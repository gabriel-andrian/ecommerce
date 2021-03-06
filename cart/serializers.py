from rest_framework import serializers
from products.serializers import ProductSerializer
from accounts.serializers import UserResumeSerializer


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cart = serializers.PrimaryKeyRelatedField(read_only=True)
    item = ProductSerializer()
    quantity = serializers.IntegerField(default=1)
    subtotal = serializers.IntegerField(default=0)


class ItemQuantitySerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1, default=1)


class CartSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    user = UserResumeSerializer()
    items = ItemSerializer(many=True)
    total = serializers.IntegerField(read_only=True)
