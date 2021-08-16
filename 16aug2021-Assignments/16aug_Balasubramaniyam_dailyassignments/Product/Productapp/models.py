from django.db import models

# Create your models here.
class Product(models.Model):
    Pcode=models.IntegerField()
    Pname=models.CharField(max_length=25)
    Pdescription=models.CharField(max_length=25)
    Pprice=models.IntegerField()