from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, pagination
from .models import Product_data
from .serializers import ProductSerializer
from .paginations import ProductPagination



class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """
    queryset = Product_data.objects.all()
    serializer_class  = ProductSerializer
    pagination_class = ProductPagination