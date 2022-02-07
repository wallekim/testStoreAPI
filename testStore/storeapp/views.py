from rest_framework import generics
from storeapp.serializers import BasketDetailSerializer, ProductListSerializer
from storeapp.models import Baskets, Products
from rest_framework import filters


class BasketCreateView(generics.CreateAPIView):
    serializer_class = BasketDetailSerializer


class BasketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasketDetailSerializer
    queryset = Baskets.objects.all()


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Products.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('price')
