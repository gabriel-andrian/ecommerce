from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Stock, Product, Transaction, Category
from .serializers import StockSerializer, ProductSerializer, TransactionSerializer, CategoriesSerializer
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from accounts.permissions import IsSeller, IsCostumer


class ProductView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug=None):

        if slug.lower() == 'avaliables':
            products = Product.objects.all()
            avaliables = []

            for product in products:
                if product.is_avaliable():
                    avaliables.append(product)

            serializer = ProductSerializer(avaliables, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        if not slug:

            return Response(status=status.HTTP_404_NOT_FOUND)

        product = get_object_or_404(Product, slug=slug.lower())
        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_staff:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = ProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product, created = Product.objects.get_or_create(
            name=request.data['name'],
            description=request.data['description'],
            price=request.data['price']
        )

        if not created:
            return Response({'message': f'Product {product.name} already exists'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        stock = Stock.objects.create(product=product)

        for category in request.data['categories']:
            category = Category.objects.get_or_create(**category)[0]
            product.categories.add(category)

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoriesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug=None):

        if not slug:
            categories = Category.objects.all()
            serializer = CategoriesSerializer(categories, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        if slug.lower() == 'products':
            query_products = Product.objects.all()

            serializer = ProductSerializer(query_products, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        category = get_object_or_404(Category, slug=slug.lower())
        products = Product.objects.all().filter(categories=category.id)

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TransactionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSeller]

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product,
                                    id=request.data['product_id'])

        serializer_transaction = TransactionSerializer(data=request.data)
        if not serializer_transaction.is_valid():
            return Response(serializer_transaction.error_messages, status=status.HTTP_400_BAD_REQUEST)

        # Talvez fazer um campo de sucess or Not sucess antes do if ou então só criar
        # a transaction dentro dos if.
        transaction = Transaction.objects.create(
            product=product, amount=request.data['amount'], transaction_type=request.data['transaction_type'])

        if transaction.transaction_type == 0:
            if product.product_stock.amount - request.data['amount'] >= 0:
                product.product_stock.amount -= request.data['amount']
                product.product_stock.save()
                return Response(data={'msg': 'Successfully Removed!'})
            return Response(data={'msg': 'Value Out Of Range!'}, status=status.HTTP_400_BAD_REQUEST)

        elif transaction.transaction_type == 1:
            product.product_stock.amount += request.data['amount']
            product.product_stock.save()
            return Response(data={'msg': 'Successfully Added!'})
