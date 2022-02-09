from storeapp.views import BasketCreateView, BasketListView, ProductListView, ProductDetailView
from django.urls import path

urlpatterns = [
    path('basket/create/', BasketCreateView.as_view(), name='bsktcreate'),
    path('basket/list/', BasketListView.as_view()),
    path('product/list/', ProductListView.as_view()),
    path('product/retrieve/<int:pk>/', ProductDetailView.as_view()),
]