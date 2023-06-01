from django.shortcuts import render, get_object_or_404
from .models import Item


# Index page with all items.
def all_items(request):
    items = Item.objects.all()
    context = {'items': items,}

    return render(request,'product/items.html', context)
