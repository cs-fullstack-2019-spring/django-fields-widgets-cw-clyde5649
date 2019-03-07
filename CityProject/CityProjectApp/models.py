from django.db import models

# Create your models here.



class CityApplication(models.Model):
    date = models.DateField(default='')
    name = models.CharField(max_length=20,default='')
    dropbox = models.CharField(max_length=200)
    checkbox = models.CharField(max_length=200)
    email = models.EmailField(default='')
    cityoforgin = models.CharField(max_length=200)
    richorsuperpowers =models.CharField(max_length=200)



