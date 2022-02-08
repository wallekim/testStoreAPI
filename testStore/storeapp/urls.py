from django.contrib import admin
from storeapp.views import BasketCreateView, BasketListlView, ProductListView
from django.urls import path, include

urlpatterns = [
    path('basket/create/', BasketCreateView.as_view()),
    path('product/list/', ProductListView.as_view()),
    path('product/retrive/<id>/', BasketCreateView.as_view()),
]