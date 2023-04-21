from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150, blank=True)
    post = models.TextField(blank=False)
    number_of_likes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username

class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.IntegerField(blank=False)

    def __str__(self):
        return self.user.username
    


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.IntegerField(blank=False)
    comment = models.CharField(blank=False, max_length=250)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username
    
    