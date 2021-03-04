from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Item(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    item = models.ForeignKey(
        Product, related_name='item_product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.PositiveIntegerField(default=0)


class Cart(models.Model):
    user = models.OneToOneField(
        User, related_name='cart_user', on_delete=models.CASCADE)
    items = models.ManyToManyField(
        'Item', related_name='cart_item', blank=True)
    total = models.PositiveIntegerField(default=0)

    def add_item(self, product, quantity=1):
        if Item.filter(cart=self.id, item=product).exists():
            create_item = False
            item = Item.objects.get(cart=cart_id, item=product)
            item.quantity = item.quantity + quantity
            item.subtotal = item.quantity * item.item.price
            item.save()
        else:
            create_item = True
            item = self.objects.create(
                cart=cart_id, item=product, quantity=quantity)
            item.subtotal = item.quantity * item.item.price
            item.save()

        return item, create
