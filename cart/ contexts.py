from decimal import Decimal
from django.conf import settings

# Context that generates the dictionary holding bag contents.
def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0

    if total < settings.FREE_SHIPPING:
        shipping = total * Decimal(settings.SHIPPING_RATE)
        to_get_free_shipping = settings.FREE_SHIPPING - total
    else:
        shipping = 0
        to_get_free_shipping = 0

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'item_count': item_count,
        'free_shipping': FREE_SHIPPING,
        'shipping': shipping,
        'to_get_free_shipping':to_get_free_shipping,
        'total': total,
        'grand_total':grand_total,
    }

    return context
