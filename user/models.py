from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# SiteUser model that holds shipping information for later
class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    siteuser_phone_number = models.CharField(max_length=20, null=True, blank=True)
    siteuser_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    siteuser_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    siteuser_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    siteuser_state = models.CharField(max_length=80, null=True, blank=True)
    siteuser_zipcode = models.CharField(max_length=20, null=True, blank=True)
    siteuser_country = CountryField(null=False, blank=False, blank_label='Select *')

    def __str__(self):
        return self.user.username

# Create siteuser profile, or update existing siteuser profile
@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if created:
        SiteUser.objects.create(user=instance)
    instance.siteuser.save()
