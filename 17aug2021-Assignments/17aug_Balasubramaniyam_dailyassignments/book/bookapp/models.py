from django.db import models

class BookModel(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    author=models.CharField(max_length=30)