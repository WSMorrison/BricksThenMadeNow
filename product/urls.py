from . import views
from django.urls import path


urlpatterns = [
     path('', views.all_items, name='items'),
]