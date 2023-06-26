from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):

    return render(request, 'cart/cart.html')


# View to add skus to customer's shopping cart
def add_to_cart(request, sku_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if sku_id in list(cart.keys()):
        cart[sku_id] += quantity
    else:
        cart[sku_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(redirect_url)

# View to adjust the quantities in the shipping cart
def adjust_cart(request, sku_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
#here
    if quantity > 0:
        cart[sku_id] = quantity
    else:
        cart.pop(sku_id)

    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(reverse('view_cart'))
