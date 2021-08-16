from django.db import models
from rest_framework import serializers
from Productapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('Pcode','Pname','Pdescription','Pprice')