# Generated by Django 4.1 on 2023-05-11 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0011_rename_itemorders_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.DeleteModel(
            name='TotalOrder',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]