from django.contrib import admin
from storeapp import models


@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Characteristics)
class CharacteristicAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Baskets)
class BasketAdmin(admin.ModelAdmin):
    pass
