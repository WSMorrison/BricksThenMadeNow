from django.conf import settings
from django.shortcuts import get_object_or_404
from product.models import Sku, Item

# Context that generates the dictionary holding bag contents.
def cart_contents(request, order_instance=None):

    cart_items = []
    total = 0
    shipping_total = 0
    item_count = 0
    cart = request.session.get('cart', {})
    item_instructions = []

    for sku_id, quantity in cart.items():
        added_sku = get_object_or_404(Sku, pk=sku_id)
        added_item = added_sku.sku_item
        added_number = added_item.item_number
        total += quantity * added_sku.sku_price
        item_count += quantity
        extended_price = quantity * added_sku.sku_price
        if added_sku.sku_physical:
            shipping_total += quantity
        cart_items.append({
            'sku_id': sku_id,
            'quantity': quantity,
            'added_sku': added_sku,
            'added_item': added_item,
            'added_number': added_number,
            'extended_price': extended_price,
        })
        item_instructions.append(added_number)

    shipping = float("{:.2f}".format(settings.GLOBAL_SHIPPING_COST))
    total = float(("{:.2f}".format(total)))
    
    grand_total = float("{:.2f}".format(total + shipping))

    context = {
        'cart_items': cart_items,
        'item_count': item_count,
        'free_shipping': settings.FREE_SHIPPING,
        'shipping': shipping,
        'to_get_free_shipping': to_get_free_shipping,
        'shipping_total': shipping_total,
        'total': total,
        'grand_total': grand_total,
        'item_instructions': item_instructions,
    }

    return context
