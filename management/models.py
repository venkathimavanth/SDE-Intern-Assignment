from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class Host(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    Email=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)

class EntryModel(models.Model):
    host=models.ForeignKey(Host, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    checkin= models.DateTimeField(auto_now_add=True)
    Description=models.CharField( max_length=1000)

class ExitModel(models.Model):
    host=models.ForeignKey(Host, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    checkin= models.DateTimeField()
    checkout=models.DateTimeField(auto_now_add=True)
    Description=models.CharField( max_length=1000)
