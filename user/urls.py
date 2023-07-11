from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.siteuser_profile, name='siteuser_profile'),
    path('orderhistory/', views.siteuser_order_history, name='siteuser_order_history'),
    # path('new_email/', views.new_email_signup, name='new_email_signup'),
]
