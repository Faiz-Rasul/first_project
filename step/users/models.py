from django.db import models
from datetime import datetime
from django.contrib.auth.models import User




# Create your models here.

class OtherRequests(models.Model):
    user = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=datetime.now)
    response = models.CharField(max_length=150, default='Response Pending')

    def __str__(self):
        return self.user
    

class UserInfo(models.Model):
    user = models.CharField(max_length=50)
    degree_title = models.CharField(max_length=20, blank=False, default='bscs')
    address = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.user


class AvailableCourses(models.Model):
    course_name = models.CharField(max_length=30, blank=False)
    course_for = models.CharField(max_length=10, default='bscs')
    course_time = models.CharField(max_length=20, default='morning')

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course1 = models.CharField(max_length=20, blank=True)
    course2 = models.CharField(max_length=20, blank=True)
    course3 = models.CharField(max_length=20, blank=True)
    course4 = models.CharField(max_length=20, blank=True)
    course5 = models.CharField(max_length=20, blank=True)
    course6 = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.user.username


class Fees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=datetime.now)
    enrollment_fees = models.IntegerField(default=5000)
    course_fees = models.IntegerField(default=0)
    monthly_fees = models.IntegerField(default=2000)
    balance = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)
    penalty = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username



class Voting(models.Model):
    option = models.CharField(blank=True, max_length=35)
    votes = models.IntegerField(default=0, blank=False)


class Votes(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.CharField(blank=True, max_length=35)
    has_voted = models.BooleanField(default=False)