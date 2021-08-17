from django.db import models
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    empcode=models.IntegerField()
    empdesignation=models.CharField(max_length=50)
    empsalary=models.IntegerField()
    
