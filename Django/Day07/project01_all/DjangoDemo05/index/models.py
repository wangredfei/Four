from django.db import models

# Create your models here.
class Users(models.Model):
    uname=models.CharField(max_length=30)
    upwd=models.CharField(max_length=30)
    uage=models.IntegerField()
    uemail=models.CharField(max_length=30)
