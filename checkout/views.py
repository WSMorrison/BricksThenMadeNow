from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import Orderform
from cart.contexts import cart_contents
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart')
    if not cart:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('items'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    stripe.PaymentIntent.create(
        amount = stripe_total,
        currency = settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NNuisE1ZJ5oC3btNsXaNlqOtMmDMMUUGQAXNIlh3WYRIeyL5A41O0fZBlpYyPuicxUAYtkpf3vQlTWgRea5B84I00mitWIOZn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
