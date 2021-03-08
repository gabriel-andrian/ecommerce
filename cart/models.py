from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import ipdb
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

    # Tirar a quantidade, só deixar add 1 item
    def add_item(self, product, quantity=1):
        stock = product.product_stock.amount
        if stock - quantity < 0:
            added = False
            return None, added

        if Item.objects.filter(cart=self.id, item=product).exists():
            item = Item.objects.get(cart=self.id, item=product)
            item.quantity = item.quantity + quantity
            item.subtotal = item.quantity * item.item.price
            item.save()
            self.items.add(item)
            self.save()

            product.product_stock.amount = stock - quantity
            product.product_stock.save()

        else:
            item = Item.objects.create(
                cart=self, item=product, quantity=quantity)
            item.subtotal = item.quantity * item.item.price
            item.save()
            self.items.add(item)
            self.save()

            product.product_stock.amount = stock - quantity
            product.product_stock.save()

        added = True
        return item, added

    def delete_item(self, product, quantity=1, order=0):
        if Item.objects.filter(cart=self.id, item=product).exists():

            item = Item.objects.get(cart=self.id, item=product)
            if item.quantity - quantity < 0:
                return False

            if item.quantity - quantity > 0 and item.quantity > 1:
                item.quantity -= quantity
                item.subtotal = item.quantity * item.item.price
                item.save()

            if item.quantity - quantity == 0:
                item.delete()

            if order == 1:
                return True

            stock = product.product_stock.amount
            product.product_stock.amount = stock + quantity
            product.product_stock.save()
            return True
        return False
