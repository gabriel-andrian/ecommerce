from rest_framework import serializers
from .utils import TRANSACTION_CHOICES


class CategoriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    url = serializers.CharField()
    created = serializers.DateField(read_only=True)
    modified = serializers.DateField(read_only=True)
    categories = CategoriesSerializer(many=True)


class StockSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    avaliable = serializers.BooleanField(read_only=True)
    amount = serializers.IntegerField()
    product_id = serializers.IntegerField(read_only=True)


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    transaction_type = serializers.ChoiceField(choices=TRANSACTION_CHOICES)
    amount = serializers.IntegerField()
    created = serializers.DateField(read_only=True)
    product_id = serializers.IntegerField()
