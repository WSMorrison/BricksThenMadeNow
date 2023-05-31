from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Item


# Index page with all items.
class AllItems(generic.ListView):
    model = Item
    queryset = Item.objects.all()
    template_name = 'index.html'
    # paginate_by = 10
