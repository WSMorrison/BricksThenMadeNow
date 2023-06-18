from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from product.models import Sku, Item

# Context that generates the dictionary holding bag contents.
def cart_contents(request):

    items = Item.objects.all()
    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for sku_id, quantity in cart.items():
        added_sku = get_object_or_404(Sku, pk=sku_id)
        added_item = added_sku.sku_item
        total += quantity * added_sku.sku_price
        item_count += quantity
        cart_items.append({
            'sku_id': sku_id,
            'quantity': quantity,
            'added_sku': added_sku,
            'added_item': added_item,
        })

    if total < settings.FREE_SHIPPING:
        shipping = total * Decimal(settings.SHIPPING_RATE)
        to_get_free_shipping = settings.FREE_SHIPPING - total
    else:
        shipping = 0
        to_get_free_shipping = 0

    grand_total = total + shipping

    context = {
        'cart_items': cart_items,
        'item_count': item_count,
        'free_shipping': settings.FREE_SHIPPING,
        'shipping': shipping,
        'to_get_free_shipping':to_get_free_shipping,
        'total': total,
        'grand_total':grand_total,
    }

    return context
