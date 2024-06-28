from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("details/<int:roomid>",views.details,name="details"),
    path("booking/<int:roomid>",views.booking,name="booking"),
    path("rental",views.rental,name="rental"),
    path("cartroom",views.cartroom,name="cartroom"),

]