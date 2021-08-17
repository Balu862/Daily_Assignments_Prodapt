from django.urls import path
from .import views
urlpatterns=[
    path('add/',views.noteadd,name="add"),
    path('viewall/',views.noteview,name="viewall"),
    path('rud/<id>',views.noterud,name="rud"),
]