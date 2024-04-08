from django.db import models


class Bill(models.Model):
    PAYMENT_MODE = [('ON', 'Online Payment'), ('OL', 'Offline Payment')]
    customer_name = models.CharField(max_length=20)
    bill_amount = models.IntegerField()
    bill_date = models.DateField()
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE)


