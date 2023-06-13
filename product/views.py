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
    current_theme = None

    if request.GET:
        if 'theme' in request.GET:
            themes = request.GET['theme'].split(',')
            items = items.filter(item_theme__name__in=themes)
            theme = Theme.objects.filter(name__in=themes)
            current_theme = get_object_or_404(theme)
        else:
            current_theme = None

        if 'searchterm' in request.GET:
            query = request.GET['searchterm']
            if not query:
                messages.error(request,'Please enter a search term.')
                return redirect(reverse('items'))
            queries = Q(item_name__icontains=query) | Q(item_description__icontains=query) | Q(item_number__icontains=query)
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

    if current_sort == "item_part_count_asc":
        current_sort = "Part Count Low to High"
    elif current_sort == "item_part_count_desc":
        current_sort = "Part Count High to Low"
    elif current_sort == "item_price_asc":
        current_sort = "Starting Price Low to High"
    elif current_sort == "item_price_desc":
        current_sort = "Starting Price High to Low"
    else:
        current_sort = "Sort by:"

    context = {'items': items, 
               'current_theme': current_theme, 
               'current_sort': current_sort
               }

    return render(request,'product/items.html', context)


# Operates page that views details about a specific item.
def item_detail(request, item_id):
    skus = Sku.objects.all()
    sku_inst = None
    sku_mdst = None
    Sku_flst = None
    item = get_object_or_404(Item, pk=item_id)

    inst = skus.filter(sku_item__in=item_id, sku_type='inst')
    try:
        sku_inst = get_object_or_404(inst)
    except:
        sku_inst = None

    mdst = skus.filter(sku_item__in=item_id, sku_type='mdst')
    try:
        sku_mdst = get_object_or_404(mdst)
    except:
        sku_mdst = None

    flst = skus.filter(sku_item__in=item_id, sku_type='flst')
    try:
        sku_flst = get_object_or_404(flst)
    except:
        sku_flst = None

    context = {'item': item,
               'sku_inst': sku_inst,
               'sku_mdst': sku_mdst,
               'sku_flst': sku_flst,
               }

    return render(request, 'product/item_detail.html', context)