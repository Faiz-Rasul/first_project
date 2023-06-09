# Generated by Django 4.1 on 2023-05-06 01:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0007_remove_postlikes_user_delete_post_delete_postlikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.IntegerField()),
                ('item_quantity', models.IntegerField(default=900000)),
                ('item_category', models.CharField(choices=[('starter', 'Starter'), ('main', 'Main'), ('drink', 'Drink'), ('desert', 'Desert'), ('other', 'Other')], max_length=50)),
                ('items_sold', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TotalOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name=datetime.datetime.now)),
                ('total_price', models.IntegerField()),
                ('extra_charges', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('tax', models.IntegerField(default=0)),
                ('bill_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name=datetime.datetime.now)),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teachers.item')),
            ],
        ),
    ]
