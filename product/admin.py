from django.contrib import admin
from .models import Theme, Item, Sku

class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'item_number',
        'item_name',
        'item_theme',
        'item_description',
        'item_old',
        'item_old_url',
        'item_render',
        'item_render_url',
        'item_modern',
        'item_modern_url',
        'item_detail',
        'item_detail_url',
        'item_part_count',
        'item_instructions_url',
    )


class SkuAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sku_item',
        'sku_number',
        'sku_type',
        'sku_price',
        'sku_physical',
        'sku_inventory',
    )


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Sku, SkuAdmin)
