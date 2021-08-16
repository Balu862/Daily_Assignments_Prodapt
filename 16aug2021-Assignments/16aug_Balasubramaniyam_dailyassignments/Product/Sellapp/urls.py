from django.urls import path
from . import views

urlpatterns=[
    path("add/",views.SellerAdd,name="SellerAdd"),
    path("views/",views.SellerView,name="Sellerview"),
]