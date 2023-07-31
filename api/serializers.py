from rest_framework import serializers
from .models import Product_data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_data
        fields = '__all__'