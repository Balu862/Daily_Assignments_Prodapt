from django.db.models import fields
from rest_framework import serializers
from bookapp.models import BookModel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        fields=('name','description','author')