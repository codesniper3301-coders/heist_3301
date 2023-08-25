from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import graph

urlpatterns = [
    path('',graph)
]