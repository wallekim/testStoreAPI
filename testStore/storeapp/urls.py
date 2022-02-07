from django.contrib import admin
from storeapp.views import BasketCreateView, BasketDetailView
from django.urls import path, include

urlpatterns = [
    path('basket/create/', BasketCreateView.as_view()),
]