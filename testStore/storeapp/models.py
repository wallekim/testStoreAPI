from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Images(models.Model):
    id = models.IntegerField(primary_key=True)
    link_to_img = models.FileField(verbose_name='Link to image', upload_to='product_img/')


class Products(models.Model):
    name = models.CharField(verbose_name='Name', max_length=256)
    price = models.IntegerField(verbose_name='Price', db_index=True)
    description = models.TextField(verbose_name='Description')
    image_id = models.ForeignKey(Images, verbose_name='Image gallery', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class Characteristics(models.Model):
    name = models.CharField(verbose_name='Name', max_length=256)
    description = models.TextField(verbose_name='Name')

    class Meta:
        verbose_name = 'characteristic'
        verbose_name_plural = 'characteristics'

    def __str__(self):
        return self.name


class ProductCharacters(models.Model):
    product_id = models.ForeignKey(Products, verbose_name='Product Id', on_delete=models.CASCADE)
    character_id = models.ForeignKey(Characteristics, verbose_name='Characteristics', on_delete=models.CASCADE)


class Baskets(models.Model):
    user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        verbose_name = 'basket'
        verbose_name_plural = 'baskets'

    def __str__(self):
        return self.user_id


class BasketProducts(models.Model):
    basket_id = models.ForeignKey(Baskets, verbose_name='Basket Id', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, verbose_name='Products Id', on_delete=models.CASCADE)
