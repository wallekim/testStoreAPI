from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from .serializers import *


class APITests(APITestCase):
    def test_create_basket(self):

        """
        Test #1
        """

        url = reverse('bsktcreate')

        user = User.objects.create_user('username', 'Pas$w0rd')
        product = Products.objects.create(name='Table', price=3000,
                                          description='The best table of the best')

        data = {
            'product_id': [product.id],
            'user_id': user.id
        }

        response = self.client.post(url, data, format='json')
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

