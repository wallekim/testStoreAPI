from rest_framework import generics
from storeapp.serializers import BasketDetailSerializer, ProductSerializer
from storeapp.models import Baskets, Products
from django_filters.rest_framework import DjangoFilterBackend


class BasketCreateView(generics.CreateAPIView):
    serializer_class = BasketDetailSerializer


class BasketListView(generics.ListAPIView):
    serializer_class = BasketDetailSerializer
    queryset = Baskets.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.prefetch_related('character').all()

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('price', 'character')


