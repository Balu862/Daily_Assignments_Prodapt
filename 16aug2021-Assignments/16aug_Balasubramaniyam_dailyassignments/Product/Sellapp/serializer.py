from rest_framework import serializers
from Sellapp.models import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('Sid','Sname','Saddress','Sphone')
