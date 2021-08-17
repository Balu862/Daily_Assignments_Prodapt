from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Notes.serializer import NotesSerializer
from Notes.models import NotesModel
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
@csrf_exempt
def noteadd(request):
    if request.method=="POST":
        notesdetail=JSONParser().parse(request)
        notesadding=NotesSerializer(data=notesdetail)
        if notesadding.is_valid():
            notesadding.save()
            print(1)
            return JsonResponse(notesadding.data,safe=False,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Details are not valid",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt

def noteview(request):
    if request.method=="GET":
        notesdetail=NotesModel.objects.all()
        notesadding=NotesSerializer(notesdetail,many=True)
        return JsonResponse(notesadding.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def noterud(request,id):
    try:
        notesdetail=NotesModel.objects.get(id=id)
        if request.method=='GET':
            notesadding=NotesSerializer(notesdetail)
            return JsonResponse(notesadding.data,safe=False,status=status.HTTP_200_OK)
        if request.method=="DELETE":
            notesdetail.delete()
            return HttpResponse("Deleted")
        if request.method=="PUT":
            notesdetails=JSONParser().parse(request)
            notesadding=NotesSerializer(data=notesdetails)
            if notesadding.is_valid():
                notesadding.save()
                return JsonResponse(notesadding.data,safe=False,status=status.HTTP_200_OK)
            else:
                return HttpResponse("data is not valid")
    except NotesModel.DoesNotExist:
        return HttpResponse("data is not available")