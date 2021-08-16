from django.db import models

# Create your models here.
class Seller(models.Model):
    Sid=models.IntegerField()
    Sname=models.CharField(max_length=20)
    Saddress=models.CharField(max_length=50)
    Sphone=models.BigIntegerField()