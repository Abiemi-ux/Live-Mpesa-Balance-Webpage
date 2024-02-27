# mpesa/urls.py

from django.urls import path
from .views import display_balance

urlpatterns = [
    path('balance/<str:user_id>/', display_balance, name='display_balance'),
]
