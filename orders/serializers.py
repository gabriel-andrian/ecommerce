from rest_framework import serializers
from accounts.serializers import UserResumeSerializer
from .utils import ORDER_STATUS
from products.serializers import ProductSerializer


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserResumeSerializer()
    status = serializers.ChoiceField(choices=ORDER_STATUS)
    created = serializers.DateField(read_only=True)


class OrderItemSerializer(serializers.Serializer):
    order = OrderSerializer()
    product = ProductSerializer()
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()


class OrderStatus(serializers.Serializer):
    order_id = serializers.IntegerField()
    status = serializers.ChoiceField(choices=ORDER_STATUS)


class OrderInfo(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserResumeSerializer()
    status = serializers.ChoiceField(choices=ORDER_STATUS)
    items_order = OrderItemSerializer()
