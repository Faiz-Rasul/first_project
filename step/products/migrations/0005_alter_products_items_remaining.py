# Generated by Django 4.1 on 2023-04-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_price_products_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='items_remaining',
            field=models.IntegerField(default=1),
        ),
    ]