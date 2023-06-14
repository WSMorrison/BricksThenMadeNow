from . import views
from django.urls import path


urlpatterns = [
     path('', views.all_items, name='items'),
     path('<item_id>', views.item_detail, name='item_detail'),
     path('add/', views.new_item, name='new_item')
]
