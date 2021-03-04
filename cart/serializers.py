from rest_framework import serializers
from products.serializers import ProductSerializer


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cart = serializers.IntegerField()
    item = ProductSerializer()
    quantity = serializers.IntegerField(default=1)
    subtotal = serializers.IntegerField(default=0)


class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # user =
    items = ItemSerializer()
    total = serializers.IntegerField(read_only=True)
