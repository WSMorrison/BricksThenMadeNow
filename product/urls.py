from . import views
from django.urls import path


urlpatterns = [
     path('', views.all_items, name='items'),
     path('<item_id>', views.item_detail, name='item_detail'),
     path('add-item/', views.new_item, name='new_item'),
     path('add-sku/', views.new_sku, name='new_sku'),
     path('edit-item/<item_id>/', views.edit_item, name='edit_item'),
     path('edit-sku/<sku_id>/', views.edit_sku, name='edit_sku'),
     path('delete-item/<item_id>/', views.delete_item, name='delete_item'),
     path('delete-sku/<sku_id>/', views.delete_sku, name='delete_sku'),
     path('confirm-delete-item/<item_id>/', views.confirm_delete_item, name='confirm_delete_item'),
     path('confirm-delete-sku/<sku_id>/', views.confirm_delete_sku, name='confirm_delete_sku'),
]
