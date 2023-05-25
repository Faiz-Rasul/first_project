from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name