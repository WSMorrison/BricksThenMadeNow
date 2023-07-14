import json
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from cart.contexts import cart_contents
from django.contrib.auth.models import User
from product.models import Sku, Item
from user.forms import SiteUserform
from user.models import SiteUser
from .forms import Orderform
from .models import Order, LineItem
from cart.contexts import cart_contents


# Holds checkout data for transmission to Stripe.
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# Manages the checkout integration with Stripe.
@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'zipcode': request.POST['zipcode'],
            'state': request.POST['state'],
            'country': request.POST['country'],
        }
        order_form = Orderform(form_data)

        if order_form.is_valid():
            cart_values = cart_contents(request)
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.shipping_cost = cart_values['shipping']
            order.save()

            for item_id, item_data in cart.items():
                try:
                    sku = Sku.objects.get(id=item_id)
                    item = sku.sku_item
                    order_line_item = LineItem(
                        order=order,
                        item=item,
                        sku=sku,
                        quantity=item_data,
                        )
                    order_line_item.save()
                except Sku.DoesNotExist:
                    messages.error(request, ('An error has occured.'))
                    order.delete()
                    return render(request, 'checkout_fail')

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'An error has occured.')
            return render(request, 'checkout_fail')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty!")
            return redirect(reverse('items'))
        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                siteuser_address_fill = SiteUser.objects.get(user=request.user)
                order_form = Orderform(initial={
                    'full_name': siteuser_address_fill.user.get_full_name(),
                    'email': siteuser_address_fill.user.email,
                    'phone_number': siteuser_address_fill.siteuser_phone_number,
                    'street_address1': siteuser_address_fill.siteuser_street_address1,
                    'street_address2': siteuser_address_fill.siteuser_street_address2,
                    'town_or_city': siteuser_address_fill.siteuser_town_or_city,
                    'state': siteuser_address_fill.siteuser_state,
                    'zipcode': siteuser_address_fill.siteuser_zipcode,
                    'country': siteuser_address_fill.siteuser_country,
                })
            except SiteUser.DoesNotExist:
                order_form = Orderform()
        else:
            order_form = Orderform()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
        return render(request, 'checkout_fail')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


# Waits for payment and order save to confirm that checkout was successful.
def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Thanks for your order #{order_number}. Get ready to build!')
    cart = request.session.get('cart')
    siteuser = request.user

    siteuser_profile = SiteUser.objects.get(user=siteuser)
    order.siteuser = siteuser_profile
    order.save()

    if save_info:
        siteuser_address = {
            'siteuser_phone_number': order.phone_number,
            'siteuser_street_address1': order.street_address1,
            'siteuser_street_address2': order.street_address2,
            'siteuser_town_or_city': order.town_or_city,
            'siteuser_state': order.state,
            'siteuser_zipcode': order.zipcode,
            'siteuser_country': order.country,
        }
        siteuser_address_form = SiteUserform(siteuser_address, instance=siteuser_profile)
        if siteuser_address_form.is_valid():
            siteuser_address_form.save()

    for item_id, item_data in cart.items():
        sku_id = Sku.objects.get(id=item_id)
        item_bought = sku_id.sku_item
        item_bought.item_user_owned.add(siteuser)
        sku_id.sku_inventory -= item_data
        sku_id.save()

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


# Handles checkout failures
def checkout_fail(request):
    template = 'checkout/checkout_fail.html'

    return render(request, template)
