from django.db import models

class NotesModel(models.Model):
    nid=models.IntegerField()
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)

