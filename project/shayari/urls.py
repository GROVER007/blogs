from django.urls import path
from shayari import views

urlpatterns = [
    path("",views.shayari)
]