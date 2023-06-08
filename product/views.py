from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Item, Theme
from django.contrib import messages
from django.db.models import Q


# Index page with all items.
def all_items(request):
    items = Item.objects.all()
    query = None
    themes = None

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

    context = {'items': items, 'current_theme': themes,}

    return render(request,'product/items.html', context)
