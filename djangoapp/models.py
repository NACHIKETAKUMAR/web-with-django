from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    Fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    dob=models.DateField()
    age=models.IntegerField()


# Create your models here.
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=30)
    dob = models.DateField()
    location = models.CharField(max_length=30)