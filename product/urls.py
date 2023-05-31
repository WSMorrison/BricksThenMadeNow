from . import views
from django.urls import path


urlpatterns = [
     path('', views.AllItems.as_view(), name='home'),
]