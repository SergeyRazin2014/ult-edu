from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer

from shop.models import Product
from shop.serializers import ProductSerializer


@api_view(['GET'])
@renderer_classes([XMLRenderer])
def product_tariff_promotion_view(request):
    products = Product.objects.prefetch_related('tariffs__promotions')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
