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

    item_added = sku.sku_item
    try:
        danger_sku = Sku.objects.get(sku_item=item_added, sku_type='inst')
    except Employee.DoesNotExist:
        danger_sku = None
    print('danger_sku', danger_sku)
    print('cartkeys', cart.keys())
    print('dangerskuid', danger_sku.id)
    if str(danger_sku.id) in list(cart.keys()):
        print('get ready to delete')
        cart[str(danger_sku.id)] = 0
        print('Instructions removed.')
        messages.success(request, "Instructions removed from cart.")

    if sku_id in list(cart.keys()):
        cart[sku_id] += quantity
    else:
        cart[sku_id] = quantity
        messages.success(request, f'Added {sku.sku_number} successfully.')

    request.session['cart'] = cart

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

    return redirect(reverse('view_cart'))


# View to remove items from the shopping cart.
def remove_cart(request, sku_id):

    cart = request.session.get('cart', {})
    cart.pop(sku_id)

    request.session['cart'] = cart
    
    return HttpResponse(status=200)
