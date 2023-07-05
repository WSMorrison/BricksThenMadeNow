from django.urls import path
from . import views

urlpatterns = [
    path('', views.siteuser_profile, name='siteuser_profile'),
]
