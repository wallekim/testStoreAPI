# Generated by Django 4.0.2 on 2022-02-07 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link_to_img', models.FileField(upload_to='product_img/', verbose_name='Link to image')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('price', models.IntegerField(db_index=True, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.images', verbose_name='Image gallery')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCharacters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.characteristics', verbose_name='Characteristics')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.products', verbose_name='Product Id')),
            ],
        ),
        migrations.CreateModel(
            name='Baskets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='BasketProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.baskets', verbose_name='Basket Id')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.products', verbose_name='Products Id')),
            ],
        ),
    ]
