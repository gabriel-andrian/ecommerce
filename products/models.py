from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from .utils import TRANSACTION_CHOICES

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(default="")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default="")
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    url = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    categories = models.ManyToManyField(
        'Category', related_name='product_categories', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def is_avaliable(self):
        if get_object_or_404(Stock, id=self.id).amount == 0:
            return False
        return True

    def __str__(self):
        return self.name


class Stock(models.Model):
    avaliable = models.BooleanField(default=False)
    amount = models.PositiveIntegerField(default=0)

    product = models.OneToOneField(
        Product, related_name='product_stock', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.amount == 0:
            self.avaliable = False
        else:
            self.avaliable = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id


class Transaction(models.Model):

    created = models.DateField(auto_now_add=True)
    amount = models.PositiveIntegerField(null=False)
    product = models.ForeignKey(
        Product, related_name='product_transactions', on_delete=models.CASCADE)
    transaction_type = models.IntegerField(
        choices=TRANSACTION_CHOICES, blank=False, null=False)

    def __str__(self):
        return f'{self.id} - Transaction Type:{self.transaction_type}'
