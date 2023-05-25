# Generated by Django 4.1 on 2023-05-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0009_totalorder_customer_name_totalorder_waiter_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemorders',
            name='order_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_category',
            field=models.CharField(choices=[('starter', 'Starter'), ('main', 'Main'), ('drink', 'Drink'), ('dessert', 'Dessert'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='itemorders',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='itemorders',
            name='total_price',
            field=models.IntegerField(default=1),
        ),
    ]