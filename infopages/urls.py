from . import views
from django.urls import path


urlpatterns = [
    path('errorpage/', views.errorpage, name='errorpage'),
    path('faq/', views.faq, name='faq'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]
