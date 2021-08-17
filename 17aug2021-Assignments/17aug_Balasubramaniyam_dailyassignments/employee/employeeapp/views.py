import re
from employeeapp.models import Employee
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from employeeapp.serializer import EmployeeSerializer
from employeeapp.models import Employee
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
# Create your views here.
@csrf_exempt
def myEmployeePage(request):
    if(request.method=="POST"):
        # getName=request.POST.get("name")
        # getCode=request.POST.get("empcode")
        # getDesignation=request.POST.get("empdesignation")
        # getSalary=request.POST.get("empsalary")
        # dict1={"name":getName,"empcode":int(getCode),'empdesignation':getDesignation,"empsalary":int(getSalary)}
        print(1)
        dict1=JSONParser().parse(request)
        result=json.dumps(dict1)
        print(result)
        employeeserial=EmployeeSerializer(data=dict1)
        #print(employeeserial.errors)
        if (employeeserial.is_valid()):
            print(1)
            employeeserial.save()
            return JsonResponse(employeeserial.data,status=status.HTTP_200_OK)
        else:
            print(employeeserial.errors)
            return HttpResponse("Not saved",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def view(request):
    if request.method=="GET":
        employeedetails=Employee.objects.all()
        employeeSerializer=EmployeeSerializer(employeedetails,many=True)
        return JsonResponse(employeeSerializer.data,safe=False)
@csrf_exempt
def Employeedetails(request,empcode):
    try:
        employeedetails=Employee.objects.get(empcode=empcode)
        if request.method=='GET':
            employeeserializer=EmployeeSerializer(employeedetails)
            return JsonResponse(employeeserializer.data,safe=False,status=status.HTTP_200_OK)
        if request.method=='DELETE':
            employeedetails.delete()
            return HttpResponse("Deleted the details")
        if request.method=='PUT':
            mydata=JSONParser().parse(request)
            employeeserializer=EmployeeSerializer(employeedetails,data=mydata)
            if (employeeserializer.is_valid()):
                employeeserializer.save()
                return JsonResponse(employeeserializer.data,status=status.HTTP_200_OK)

    except Employee.DoesNotExist:
        return HttpResponse("Invalid Employee Details",status=status.HTTP_404_NOT_FOUND)
    
'''create django project product 
create 2 apps 1)productapp
            2) Sellup
            1)adding products in product app(pcode,pname,descrpition,price,)
            2)view all

            2)seller app
            1)
            api to insert and retrive products'''