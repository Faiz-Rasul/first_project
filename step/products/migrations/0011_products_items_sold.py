# Generated by Django 4.1 on 2023-05-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_orders_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='items_sold',
            field=models.IntegerField(default=0),
        ),
    ]