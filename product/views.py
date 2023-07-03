from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item, Theme, Sku
from .forms import ItemForm, SkuForm


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
            queries = Q(item_name__icontains=query
                        ) | Q(item_description__icontains=query
                        ) | Q(item_number__icontains=query
                        )
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
    sku_flst = None
    item = get_object_or_404(Item, pk=item_id)

    try:
        sku_inst = skus.get(sku_item=item, sku_type='inst')
    except:
        sku_inst = None
    try:
        sku_mdst = skus.get(sku_item=item, sku_type='mdst')
    except:
        sku_mdst = None
    try:
        sku_flst = skus.get(sku_item=item, sku_type='flst')
    except:
        sku_flst = None

    context = {'item': item,
               'sku_inst': sku_inst,
               'sku_mdst': sku_mdst,
               'sku_flst': sku_flst,
               }

    return render(request, 'product/item-detail.html', context)


# Operates page that staff users can use to add new items to the database.
@login_required
def new_item(request):
    if not request.user.is_superuser:
        messages.error(request, 'You\'re not allowed to be here.')
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Item added, thank you.')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(request, 'Something went wrong, please check the form fields.')
    else:
        form = ItemForm()

    template = 'product/new-item.html'
    context = {'form': form,}

    return render(request, template, context)

# Operates page that staff users can use to add new items to the database.
@login_required
def new_sku(request):
    if not request.user.is_superuser:
        messages.error(request, 'You\'re not allowed to be here.')
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = SkuForm(request.POST, request.FILES)
        if form.is_valid():
            sku = form.save()
            messages.success(request, 'Sku added, thank you.')
            print(sku.sku_type)
            return redirect(reverse('items'))
        else:
            messages.error(request, 'Something went wrong, please check the form fields.')
    else:
        form = SkuForm()

    template = 'product/new-sku.html'
    context = {'form': form,}

    return render(request, template, context)
