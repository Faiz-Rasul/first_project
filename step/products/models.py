from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Products(models.Model):

    CATEGORY_CHOICES = [
        ('study', 'Study'),
        ('notes', 'Notes'),
        ('book', 'Book'),
        ('other', 'Other')
        # Add more categories here
    ]
      
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product_name = models.CharField(default='new product', blank=False, max_length=50)
    product_price = models.IntegerField(blank=False)
    product_category = models.CharField(choices=CATEGORY_CHOICES, default='study', max_length=50)
    product_image = models.ImageField(upload_to='product_images',  default='download.png' )
    items_remaining = models.IntegerField(blank=False, default=1)
    items_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username+ " - " + self.product_name
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    number_of_items = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return self.user.username+ " - " +self.product.product_name


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default=datetime.now)
    number_of_items = models.IntegerField(blank=False)
    total_price = models.IntegerField(blank=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.product.product_name

