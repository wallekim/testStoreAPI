# Generated by Django 4.0.2 on 2022-02-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_alter_images_options_alter_images_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(max_length=64, null=True, verbose_name='Name'),
        ),
    ]
