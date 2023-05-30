from django.contrib import admin
from .models import Theme, Item, Sku

# Register your models here.
admin.site.register(Theme)
admin.site.register(Item)
admin.site.register(Sku)