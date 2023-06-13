from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Item, Theme, Sku
from django.contrib import messages
from django.db.models import Q


# Operates the index page with all items.
def all_items(request):
    items = Item.objects.all()
    query = None
    themes = None
    sort = None
    direction = None

    if request.GET:
        if 'theme' in request.GET:
            themes = request.GET['theme'].split(',')
            items = items.filter(item_theme__name__in=themes)
            themes = Theme.objects.filter(name__in=themes)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,'Please enter a search term.')
                return redirect(reverse('items'))
            queries = Q(item_name__icontains=query) | Q(item_description__icontains=query)
            items = items.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

    current_sort = f'{sort}_{direction}'

    context = {'items': items, 
               'current_theme': themes, 
               # 'current_sort': current_sort
               }

    return render(request,'product/items.html', context)


# Operates page that views details about a specific item.
def item_detail(request, item_id):
    skus = Sku.objects.all()
    item = get_object_or_404(Item, pk=item_id)

    sku_inst = skus.filter(sku_item__in=item_id, sku_type='inst').values()
    sku_mdst = skus.filter(sku_item__in=item_id, sku_type='mdst').values()
    sku_flst = skus.filter(sku_item__in=item_id, sku_type='flst').values()

    context = {'item': item,
               'sku_inst': sku_inst,
               'sku_mdst': sku_mdst,
               'sku_flst': sku_flst,
               }

    return render(request, 'product/item_detail.html', context)