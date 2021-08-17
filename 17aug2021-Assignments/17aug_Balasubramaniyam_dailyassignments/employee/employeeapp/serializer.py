from rest_framework import serializers
from employeeapp.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('name','empcode','empdesignation','empsalary')