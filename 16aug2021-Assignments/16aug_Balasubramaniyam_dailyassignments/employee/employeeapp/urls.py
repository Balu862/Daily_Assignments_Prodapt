from django.urls import path,include
from .import views

urlpatterns=[
    path("add/",views.myEmployeePage,name="Employee"),
    path("view/",views.view,name="emolyee_details")

]