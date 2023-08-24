from django.urls import path
from .views import handlelogin
urlpatterns = [
    path('',handlelogin,name='login'),
]
