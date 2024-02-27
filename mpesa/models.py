from django.db import models

# Create your models here.
# mpesa/models.py

class MpesaBalance(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user_id} - ${self.balance}"
