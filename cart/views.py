from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Cart, Item
from .serializers import CartSerializer, ItemSerializer, ItemQuantitySerializer
from products.serializers import ProductSerializer

from products.models import Product, Stock
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from accounts.permissions import IsSeller, IsCostumer


class CartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCostumer]

    def get(self, request):
        user_id = request.user.id
        cart = get_object_or_404(Cart, user=user_id)

        serializer = CartSerializer(cart)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CartItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCostumer]

    def post(self, request, slug):
        user_id = request.user.id

        quantity = ItemQuantitySerializer(data=request.data)

        if not quantity.is_valid():
            return Response(data=quantity.errors, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, slug=slug.lower())

        productSerializer = ProductSerializer(product)

        user = get_object_or_404(User, id=user_id)

        cart = Cart.objects.get_or_create(user=user)[0]
        item, added = cart.add_item(
            product=product, quantity=quantity.data['quantity'])

        if not added:
            return Response(data={'msg:': 'Out of stock range'}, status=status.HTTP_401_UNAUTHORIZED)

        total = 0
        for item in cart.item_set.all():
            print(item)
            total += item.subtotal

        cart.total = total
        cart.save()
        serializer = ItemSerializer(item)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, slug):
        user_id = request.user.id

        quantity = ItemQuantitySerializer(data=request.data)

        if not quantity.is_valid():
            return Response(data=quantity.errors, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, slug=slug.lower())

        productSerializer = ProductSerializer(product)

        user = get_object_or_404(User, id=user_id)

        cart = get_object_or_404(Cart, user=user)
        removed = cart.delete_item(
            product=product, quantity=quantity.data['quantity'])

        if not removed:
            return Response(data={'msg': "Product doesn't exist in cart or quantity not acceptable"}, status=status.HTTP_400_BAD_REQUEST)

        total = 0
        for item in cart.item_set.all():
            total += item.subtotal

        cart.total = total

        cart.save()

        return Response(status=status.HTTP_200_OK)
