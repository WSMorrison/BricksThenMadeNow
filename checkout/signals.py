from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import LineItem


@receiver(post_save, sender=LineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, sender=LineItem)
def update_on_save(sender, instance, **kwargs):
    instance.order.update_total()