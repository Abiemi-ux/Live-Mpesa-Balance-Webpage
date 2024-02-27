# from django.shortcuts import render

# # Create your views here.
# # mpesa/views.py

# from .models import MpesaBalance

# def display_balance(request, user_id):
#     try:
#         mpesa_balance = MpesaBalance.objects.get(user_id=user_id)
#         balance_amount = mpesa_balance.balance
#     except MpesaBalance.DoesNotExist:
#         balance_amount = 0  # Set a default value or handle accordingly

#     return render(request, 'mpesa/balance.html', {'balance_amount': balance_amount})

# mpesa/views.py

from django.shortcuts import render
from .models import MpesaBalance
import requests  # Add this import for making API requests

def display_balance(request, user_id):
    try:
        mpesa_balance = MpesaBalance.objects.get(user_id=user_id)
        api_key = mpesa_balance.api_key

        # Make a request to the M-Pesa API to get balance
        api_url = 'https://api.example.com/mpesa/balance'  # Replace with the actual API endpoint
        headers = {'Authorization': f'Bearer {api_key}'}

        response = requests.get(api_url, headers=headers)
        data = response.json()

        # Update the balance in the database
        mpesa_balance.balance = data.get('balance', 0)
        mpesa_balance.save()

        balance_amount = mpesa_balance.balance
    except MpesaBalance.DoesNotExist:
        balance_amount = 0  # Set a default value or handle accordingly

    return render(request, 'mpesa/balance.html', {'balance_amount': balance_amount})
