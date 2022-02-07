from rest_framework import serializers
from storeapp.models import Baskets, Products


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'price', 'description')


class BasketDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Baskets
        fields = '__all__'
