from employeeapp.models import Employee
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from employeeapp.serializer import EmployeeSerializer
from employeeapp.models import Employee
import json
# Create your views here.
@csrf_exempt
def view(request):
    if request.method=="GET":
        employeedetails=Employee.objects.all()
        employeeSerializer=EmployeeSerializer(employeedetails,many=True)
        return JsonResponse(employeeSerializer.data,safe=False)

def myEmployeePage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getCode=request.POST.get("empcode")
        getDesignation=request.POST.get("empdesignation")
        getSalary=request.POST.get("empsalary")
        dict1={"name":getName,"empcode":int(getCode),'empdesignation':getDesignation,"empsalary":int(getSalary)}
        result=json.dumps(dict1)
        print(result)
        employeeserial=EmployeeSerializer(data=dict1)
        #print(employeeserial.errors)
        if (employeeserial.is_valid()):
            print(1)
            employeeserial.save()
            return JsonResponse(employeeserial.data)
        else:
            print(employeeserial.errors)
            return HttpResponse("Not saved")


'''create django project product 
create 2 apps 1)productapp
            2) Sellup
            1)adding products in product app(pcode,pname,descrpition,price,)
            2)view all

            2)seller app
            1)
            api to insert and retrive products'''