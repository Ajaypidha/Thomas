from turtle import heading
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(null=True,blank=True)
    heading=models.CharField(null=True,blank=True)
    description=models.CharField(null=True,blank=True)