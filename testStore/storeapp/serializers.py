from rest_framework import serializers
from storeapp.models import Baskets, Products, Characteristics


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    character = CharacterSerializer(many=True)

    class Meta:
        model = Products
        fields = '__all__'


class BasketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baskets
        fields = '__all__'
