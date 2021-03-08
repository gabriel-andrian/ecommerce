from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from .utils import ORDER_STATUS, ORDERED

# Create your models here.


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    status = models.IntegerField(
        choices=ORDER_STATUS, blank=False, null=False, default=ORDERED)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'<Pedido {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, related_name='items_order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
