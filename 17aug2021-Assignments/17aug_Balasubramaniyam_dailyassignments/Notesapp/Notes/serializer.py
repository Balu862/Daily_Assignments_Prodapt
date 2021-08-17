from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from Notes.models import NotesModel

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotesModel
        fields=('nid','name','description')