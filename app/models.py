from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    mobile_no = models.CharField(max_length=12)
    adress = models.CharField(max_length=100)                              
    
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=50)
    salary = models.IntegerField()
    
    def __str__(self):
        return self.name
    