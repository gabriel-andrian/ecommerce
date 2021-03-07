from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Product, Stock
from cart.models import Cart
from .models import Order, OrderItem
from .models import Order
from .serializers import OrderSerializer, OrderItemSerializer

import ipdb


class OrderView(APIView):
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
            cart.delete_item(product.item, product.quantity)

        cart.delete()
        return Response(data=serializer.data)


# Fazer o path de mudar o state ( não considerar o delete aqui)

# Fazer o delete que é para mudar o state delete e voltar no stock os produtos
