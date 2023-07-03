from . import views
from django.urls import path


urlpatterns = [
     path('', views.all_items, name='items'),
     path('<item_id>', views.item_detail, name='item_detail'),
     path('add-item/', views.new_item, name='new_item'),
     path('add-sku/', views.new_sku, name='new_sku'),
]
