from django.db import models
from .utils import TRANSACTION_CHOICES

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    avaliable = models.BooleanField(default=False)
    amount = models.PositiveIntegerField(default=0)

    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='product_stock')

    def is_avaliable():
        if (amount > 0):
            return True

        return False

    def __str__(self):
        return self.id


class Transaction(models.Model):

    created = models.DateField(auto_now_add=True)
    amount = models.PositiveIntegerField(null=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_transactions')
    transaction_type = models.IntegerField(
        choices=TRANSACTION_CHOICES, blank=False, null=False)

    def __str__(self):
        return f'{self.id} - Transaction Type:{self.transaction_type}'
