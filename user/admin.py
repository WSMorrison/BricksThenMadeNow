from django.contrib import admin
from .models import SiteUser, NewsletterUser


class SiteUserAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'siteuser_zipcode',
    )

class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = (
        'newsletter_name',
        'newsletter_email',
        'newsletter_city',
        'newsletter_space',
        'newsletter_castle',
        'newsletter_train',
    )

admin.site.register(SiteUser, SiteUserAdmin)
admin.site.register(NewsletterUser, NewsletterUserAdmin)
