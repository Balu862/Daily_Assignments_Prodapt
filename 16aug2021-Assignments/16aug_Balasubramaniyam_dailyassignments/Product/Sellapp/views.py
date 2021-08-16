from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Sellapp.models import Seller
from Sellapp.serializer import SellerSerializer
from django.http import JsonResponse,HttpResponse
@csrf_exempt
def SellerAdd(request):
    if request.method=="POST":
        sid=request.POST.get("sid")
        sname=request.POST.get("sname")
        saddress=request.POST.get("saddress")
        sphone=request.POST.get("sphone")
        dict1={'Sid':sid,'Sname':sname,'Saddress':saddress,'Sphone':sphone}
        sellerserializer=SellerSerializer(data=dict1)
        print(sellerserializer)
        if sellerserializer.is_valid():
            sellerserializer.save()
            return JsonResponse(sellerserializer.data)
        else:
            print(sellerserializer)
            return JsonResponse(sellerserializer.errors)

def SellerView(request):
    if request.method=='GET':
        sellerdetails=Seller.objects.all()
        sellerserializer=SellerSerializer(sellerdetails,many=True)
        return JsonResponse(sellerserializer.data,safe=False)
