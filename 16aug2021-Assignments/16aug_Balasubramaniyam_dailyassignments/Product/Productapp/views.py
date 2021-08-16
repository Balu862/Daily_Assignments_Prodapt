from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from Productapp.serializer import ProductSerializer
from Productapp.models import Product
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def ProductAdd(request):
    if request.method=="POST":
        pcode=request.POST.get('pcode')
        pname=request.POST.get('pname')
        pdescription=request.POST.get('pdescription')
        pprice=request.POST.get('pprice')
        dict1={'Pcode':int(pcode),'Pname':pname,'Pdescription':pdescription,'Pprice':int(pprice)}
        productserializer=ProductSerializer(data=dict1)
        print(productserializer)
        if productserializer.is_valid():
            productserializer.save()
            return JsonResponse(productserializer.data)
        else:
            print(productserializer.errors)
            return JsonResponse(productserializer.errors)
    else:
        return HttpResponse("Get Method is not Valid")
def ProductView(request):
    if request.method=="GET":
        productdetails=Product.objects.all()
        productserializer=ProductSerializer(productdetails,many=True)
        return JsonResponse(productserializer.data,safe=False)
