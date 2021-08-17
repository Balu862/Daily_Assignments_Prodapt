from django.urls import path
from . import views
urlpatterns=[
    path('add/',views.BookAdd,name="addbook"),
    path('viewall/',views.BookAll,name="viewBookall"),
    path("crud/<id>",views.BookCrud,name="Crud"),
]