from django.db import models
from django.core.exceptions import ValidationError


def validate_inventory(value):
    if value >= 0:
        return value
    else:
        raise ValidationError('Inventory must be 0, or a positive number.')


class Theme(models.Model):
    name = models.CharField(max_length=10)


class Item(models.Model):
    item_number = models.CharField(max_length=7, unique=True)
    item_name = models.CharField(max_length=40)
    item_theme = models.ForeignKey(Theme, on_delete=models.SET_DEFAULT, default='MOC')
    item_description = models.TextField(max_length=250)
    item_old = models.ImageField(null=True, blank=True)
    item_old_url = models.URLField(max_length=1024, null=True, blank=True)
    item_render = models.ImageField(null=True, blank=True)
    item_render_url = models.URLField(max_length=1024, null=True, blank=True)
    item_modern = models.ImageField(null=True, blank=True)
    item_modern_url = models.URLField(max_length=1024, null=True, blank=True)
    item_detail = models.ImageField(null=True, blank=True)
    item_detail_url = models.URLField(max_length=1024, null=True, blank=True)
    item_part_count = models.IntegerField()


class Sku(models.Model):
    sku_type_choices = [
        ('inst', 'Instructions Only'),
        ('mdst', 'Modern Set with Bricks'),
        ('flst', 'Full Set with Modern Set and Vintage Set Bricks'),
    ]
    sku_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sku_number = models.CharField(max_length=5)
    sku_type = models.CharField(max_length=4,
                                choices=sku_type_choices,
                                default='inst')
    sku_price = models.DecimalField(max_digits=6, decimal_places=2)
    sku_physical = models.BooleanField(default=False)
    sku_inventory = models.IntegerField(validators=[validate_inventory])
