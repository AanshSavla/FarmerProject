from django.urls import path
from . import views

urlpatterns = [
    path('farmerLogin',views.farmerLogin,name='farmerLogin'),
    path('farmerLogin/getFarmer',views.getFarmer,name='getFarmer'),
    path('farmReg/farmer_insert',views.farmer_insert,name='farmer_insert'),
    path('farmReg/',views.farmReg,name='farmReg'),
    path('farmerLogin/getRate',views.getRate,name='getRate'),
    path('customerLogin/getRate',views.getRate,name='getRate'),
    path('customerReg/customer_insert',views.customer_insert,name='customer_insert'),
    path('customerReg/',views.customerReg,name='customerReg'),
    path('customerLogin',views.customerLogin,name='customerLogin'), 
    path('customerLogin/getFarmer',views.getFarmer,name='getFarmer'),
    path('',views.home,name='home'),
]