from django.urls import path
from .views import home,get_stock_price
urlpatterns = [
    path('',home,name='home'),
    path('get_stock_price/', get_stock_price, name='get_stock_price'),
    

 ]
