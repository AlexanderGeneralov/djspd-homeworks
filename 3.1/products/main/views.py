from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Product, Review
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)


@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    ser = ReviewSerializer(reviews, many=True)
    return Response(ser.data)


@api_view(['GET'])
def product_details_view(requeset):
    product = Product.objects.get(id=1)
    ser = ProductDetailsSerializer(product)
    return Response(ser.data)


class ProductDetailsView(APIView):

    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        try:
            product = Product.objects.get(pk=product_id)

            ser = ProductDetailsSerializer(product, many=False)
            return Response(ser.data)
        except Product.DoesNotExist:
            raise Http404('Product not found')


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""

        mark_val = request.query_params.get('mark')

        product = Product.objects.filter(pk=product_id, comments__mark=mark_val)
        ser = ProductDetailsSerializer(product, many=False)
        return Response(ser.data)

