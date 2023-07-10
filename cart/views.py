from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from product.models import Sku

# View cart.
def view_cart(request):

    return render(request, 'cart/cart.html')


# View to add skus to customer's shopping cart.
def add_to_cart(request, sku_id):

    sku = Sku.objects.get(pk=sku_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if sku_id in list(cart.keys()):
        cart[sku_id] += quantity
    else:
        cart[sku_id] = quantity
        messages.success(request, f'Added {sku.sku_number} successfully.')

    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(redirect_url)


# View to adjust the quantities in the shopping cart.
def adjust_cart(request, sku_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[sku_id] = quantity
    else:
        cart.pop(sku_id)

    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(reverse('view_cart'))


# View to remove items from the shopping cart.
def remove_cart(request, sku_id):

    cart = request.session.get('cart', {})
    cart.pop(sku_id)

    request.session['cart'] = cart
    print(request.session['cart'])

    return HttpResponse(status=200)
