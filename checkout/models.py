import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from django.http import HttpRequest
from product.models import Item, Sku
from user.models import SiteUser
from cart.contexts import cart_contents


# Order model including customer information.
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    siteuser = models.ForeignKey(SiteUser, on_delete=models.SET_NULL,
                                 null=True, blank=True, related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    state = models.CharField(max_length=80, null=False, blank=False)
    zipcode = models.CharField(max_length=20, null=True, blank=False)
    country = CountryField(null=False, blank=False, blank_label='Select *')
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = float("{:.2f}".format(self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0))
        self.shipping_cost = float("{:.2f}".format(settings.GLOBAL_SHIPPING_COST))
        self.grand_total = float("{:.2f}".format(self.order_total + self.shipping_cost))
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# Lineitem model for each item added to the order.
class LineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE,
                              related_name='lineitems')
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    sku = models.ForeignKey(Sku, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.sku.sku_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.sku.sku_number} on order {self.order.order_number}'
