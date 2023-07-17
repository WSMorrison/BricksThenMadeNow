from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item, Theme, Sku
from .forms import ItemForm, SkuForm


# Operates the index page with all items.
def all_items(request):
    items = Item.objects.all().order_by('item_number')
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
                messages.error(request, 'Please enter a search term.')
                return redirect(reverse('items'))
            queries = Q(item_name__icontains=query) | Q(
                        item_description__icontains=query) | Q(
                        item_number__icontains=query)
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

    return render(request, 'product/items.html', context)


# Operates page that views details about a specific item.
def item_detail(request, item_id):
    skus = Sku.objects.all()
    sku_inst = None
    sku_mdst = None
    sku_flst = None
    item = get_object_or_404(Item, pk=item_id)

    try:
        sku_inst = skus.get(sku_item=item, sku_type='inst')
    except Exception as e:
        sku_inst = None
        messages.error(request, f'No instructions: {e}')
        return HttpResponse(status=500)
    try:
        sku_mdst = skus.get(sku_item=item, sku_type='mdst')
    except Exception as e:
        sku_mdst = None
        messages.error(request, f'No Modernset: {e}')
        return HttpResponse(status=500)
    try:
        sku_flst = skus.get(sku_item=item, sku_type='flst')
    except Exception as e:
        sku_flst = None
        messages.error(request, f'No FullSet: {e}')
        return HttpResponse(status=500)

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
            messages.error(request, 'Please check the form fields.')
    else:
        form = ItemForm()

    template = 'product/new-item.html'
    context = {'form': form, }

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
            input_form = form.instance
            input_sku = form.instance.sku_type
            input_item = form.instance.sku_item
            item_skus = Sku.objects.all().filter(sku_item=input_item)
            danger_sku = item_skus.filter(sku_type=input_sku)
            if danger_sku:
                messages.error(request, 'Sku exists, check your inputs.')
                form = SkuForm(instance=input_form)
            else:
                form.save()
                messages.success(request, 'Sku added, thank you.')
                return redirect(reverse('items'))
        else:
            messages.error(request, 'Please check the form fields.')
    else:
        form = SkuForm()

    template = 'product/new-sku.html'
    context = {'form': form, }

    return render(request, template, context)


# Operates page that staff users can use to edit items in the database.
@login_required
def edit_item(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'You\'re not allowed to be here.')
        return redirect(reverse('index'))

    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item record updated.')
            return redirect(reverse('item_detail', args=[item_id]))
        else:
            messages.error(request, 'Item update FAILED.')

    else:
        form = ItemForm(instance=item)

    template = 'product/edit-item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


# Operates page that staff users can use to edit items in the database.
@login_required
def edit_sku(request, sku_id):
    if not request.user.is_superuser:
        messages.error(request, 'You\'re not allowed to be here.')
        return redirect(reverse('index'))

    sku = get_object_or_404(Sku, pk=sku_id)
    item = sku.sku_item
    item_id = item.id
    if request.method == 'POST':
        form = SkuForm(request.POST, request.FILES, instance=sku)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sku record updated.')
            return redirect(reverse('item_detail', args=[item_id]))
        else:
            messages.error(request, 'Sku update FAILED.')

    else:
        form = SkuForm(instance=sku)

    template = 'product/edit-sku.html'
    context = {
        'form': form,
        'sku': sku,
    }

    return render(request, template, context)


# Double checks that user intends Item deletion.
@login_required
def delete_item(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'You\'re not allowed to be here.')
        return redirect(reverse('index'))

    template = 'product/confirm-delete-item.html'
    context = {
        'item_id': item_id,
    }

    return render(request, template, context)


# Double checks that user intends Sku deletion.
@login_required
def delete_sku(request, sku_id):
    if not request.user.is_superuser:
        messages.error(request, 'You\'re not allowed to be here.')
        return redirect(reverse('index'))

    template = 'product/confirm-delete-sku.html'
    context = {
        'sku_id': sku_id,
    }

    return render(request, template, context)


# Performs the item deletion.
@login_required
def confirm_delete_item(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'You\'re not allowed to be here.')
        return redirect(reverse('index'))

    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.info(request, 'Successfully deleted item.')

    items = Item.objects.all()
    context = {
        'items': items,
    }

    return render(request, 'product/items.html', context)


# Performs the sku deletion.
@login_required
def confirm_delete_sku(request, sku_id):
    if not request.user.is_superuser:
        messages.error(request, 'You\'re not allowed to be here.')
        return redirect(reverse('index'))

    sku = get_object_or_404(Sku, pk=sku_id)
    sku.delete()
    messages.info(request, 'Successfully deleted sku.')

    items = Item.objects.all()
    context = {
        'items': items,
    }

    return render(request, 'product/items.html', context)


# Handles error page.
def errorpage(request):
    return render(request, 'errorpage.html')
