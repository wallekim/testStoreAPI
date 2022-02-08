from django.contrib import admin
from storeapp import models


@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_display_links = ('name', 'price')
    list_filter = ('name', 'price', 'description')


@admin.register(models.Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('name',)


@admin.register(models.Characteristics)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('name',)


@admin.register(models.Baskets)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'date')
    list_filter = ('id', 'user_id', 'date')
    list_display_links = ('id', 'user_id', 'date')