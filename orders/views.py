from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Product, Stock
from cart.models import Cart
from .models import Order, OrderItem
from .models import Order
from .serializers import OrderSerializer, OrderItemSerializer, OrderStatus, OrderInfo

import ipdb


class OrderView(APIView):
    def get(self, request):
        order = get_object_or_404(Order, id=request.data['order_id'])
        serializer = OrderSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        cart = get_object_or_404(Cart, user_id=request.data['user_id'])
        user = get_object_or_404(User, id=request.data['user_id'])
        order = Order.objects.create(user=user)
        for item in cart.item_set.all():
            orderItem = OrderItem.objects.create(
                order=order, product=item.item, quantity=item.quantity, price=item.item.price)

        items_order = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(items_order, many=True)

        for product in cart.item_set.all():
            cart.delete_item(product.item, product.quantity, 1)

        cart.delete()
        return Response(data=serializer.data)

    def put(self, request):
        serializer = OrderStatus(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        order = get_object_or_404(Order, id=request.data['order_id'])

        if order.status == 4:
            return Response(data={'msg': 'Order has already been canceled'}, status=status.HTTP_403_FORBIDDEN)

        if request.data['status'] == 4:
            items = order.items_order.all()

            for item in items:
                stock = get_object_or_404(Stock, product_id=item.product_id)
                stock.amount += item.quantity
                stock.save()

            order.status = request.data['status']
            order.save()

            return Response(data={'msg': f'Order {order.id} canceled'}, status=status.HTTP_200_OK)

        order.status = request.data['status']
        order.save()

        serializer = OrderSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
