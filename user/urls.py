from django.urls import path
from . import views

urlpatterns = [
    path('profile/',
         views.siteuser_profile,
         name='siteuser_profile'),
    path('orderhistory/',
         views.siteuser_order_history,
         name='siteuser_order_history'),
    path('newsletter_signup/',
         views.newsletter_signup,
         name='newsletter_signup'),
]
