from django.contrib import admin
from storeapp.views import BasketCreateView, BasketListView, ProductListView, ProductDetailView
from django.urls import path, include

urlpatterns = [
    path('basket/create/', BasketCreateView.as_view(), name='bsktcreate'),
    path('product/list/', ProductListView.as_view()),
    path('product/retrieve/<int:pk>/', ProductDetailView.as_view()),
]