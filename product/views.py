from django.shortcuts import render, get_object_or_404
from .models import Item, Theme


# Index page with all items.
def all_items(request):
    items = Item.objects.all()
    themes = None

    if request.GET:
        if 'theme' in request.GET:
            themes = request.GET['theme'].split(',')
            items = items.filter(item_theme__name__in=themes)
            themes = Theme.objects.filter(name__in=themes)

    context = {'items': items, 'current_theme': themes,}
    print(themes)

    return render(request,'product/items.html', context)
