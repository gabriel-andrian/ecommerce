from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Stock, Product, Transaction, Category
from .serializers import StockSerializer, ProductSerializer, TransactionSerializer, CategoriesSerializer
# Create your views here.
import ipdb


class ProductView(APIView):

    def get(self, request, slug=None):

        if not slug:
            query_products = Product.objects.all()

            serializer = ProductSerializer(query_products, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        product = get_object_or_404(Product, slug=slug.lower())

        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Se o nome for igual esta retornando error 500, trocar.
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

    # Delete apagando tabela Transaction (não pode)
    # def delete(self, request, slug):

    #     product = Product.objects.get(id=1)
    #     product.delete()
    #     return Response(data="ok", status=status.HTTP_200_OK)


class CategoriesView(APIView):
    def get(self, request, slug=None):

        if not slug:
            categories = Category.objects.all()
            serializer = CategoriesSerializer(categories, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        category = get_object_or_404(Category, slug=slug.lower())
        products = Product.objects.all().filter(categories=category.id)

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TransactionView(APIView):
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
                return Response(data={'msg': 'Tirado com sucesso'})
            return Response(data={'msg': 'Valor negativo no stock'})

        elif transaction.transaction_type == 1:
            product.product_stock.amount += request.data['amount']
            product.product_stock.save()
            return Response(data={'msg': 'Adicionado com sucesso'})


class TesteView(APIView):
    def get(self, request, slug):
        category_slug = slug
        ipdb.set_trace()
        return Response(data={'msg': category_slug}, status=status.HTTP_200_OK)