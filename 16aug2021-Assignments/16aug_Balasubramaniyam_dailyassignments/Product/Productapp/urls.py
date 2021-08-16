from django.urls import path,include
from . import views

urlpatterns=[
    path('add/',views.ProductAdd,name="prdouctadd"),
    path('view/',views.ProductView,name="productview"),
]