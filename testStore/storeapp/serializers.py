from rest_framework import serializers
from storeapp.models import Baskets, Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class BasketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baskets
        fields = '__all__'
