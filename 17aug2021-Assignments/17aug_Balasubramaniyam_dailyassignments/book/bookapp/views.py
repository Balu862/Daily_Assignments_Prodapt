import re
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from bookapp.models import BookModel
from bookapp.serializer import BookSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
@csrf_exempt
def BookAdd(request):
    if request.method=="POST":
        bookdetails=JSONParser().parse(request)
        Bookdata=BookSerializer(data=bookdetails)
        if Bookdata.is_valid():
            Bookdata.save()
            return JsonResponse(Bookdata.data,safe=False,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Entered details are not Valid",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Please check Your request method")

@csrf_exempt
def BookAll(request):
    if request.method=="GET":
        bookdetails=BookModel.objects.all()
        bookdata=BookSerializer(bookdetails,many=True)
        return JsonResponse(bookdata.data,safe=False,status=status.HTTP_200_OK)


@csrf_exempt
def BookCrud(request,id):
    try:
        bookdata=BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        return HttpResponse("Data is not present in Collection")
    if request.method=="GET":
        bookdetails=BookSerializer(bookdata)
        return JsonResponse(bookdetails.data,status=status.HTTP_200_OK)
    if request.method=="DELETE":
        bookdata.delete()
        return HttpResponse("Deleted successfully",status=status.HTTP_200_OK)

    if request.method=="PUT":
        bookdata=JSONParser().parse(request)
        bookdetails=BookSerializer(data=bookdata)
        if bookdetails.is_valid():
            bookdetails.save()
            return JsonResponse(bookdetails.data,safe=True,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Data is not valid")