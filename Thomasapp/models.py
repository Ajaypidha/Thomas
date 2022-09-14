from turtle import heading
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(null=True,blank=True)
    heading=models.CharField(null=True,blank=True)
    description1=models.CharField(null=True,blank=True)
    description2=models.CharField(null=True,blank=True)
    description3=models.CharField(null=True,blank=True)
    description4=models.CharField(null=True,blank=True)
    school=models.CharField(null=True,blank=True)

    product=models.CharField(null=True,blank=True)
    apple=models.CharField(null=True,blank=True)
    bisk=models.CharField(null=True,blank=True)
      

      


    



