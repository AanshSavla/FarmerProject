from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Farmers,Customers
from passlib.hash import pbkdf2_sha256
import requests


# Create your views here.

def home(request):
    return render(request,'home.html')

def farmReg(request):
    return render(request,'farmerReg.html')

def getRate(request):
    if request.method=='POST':
        url='https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001b521938e016840536cdbb062e36cbb48&format=json&offset=0&limit=1500&filters[commodity]='+request.POST['crop']
        #+'&filters[state]='+request.POST['state']
        r = requests.get(url)
        rate = r.json()
        l1 = rate['records']
        return render(request,'rate.html',{'rate':l1})
    else:
        return render(request,'rate.html')

def getFarmer(request):
    farmers=[]
    if request.method == 'POST':
     
        farmers.append(Farmers.objects.filter(state=request.POST['state'],crop1=request.POST['crop']))
        farmers.append(Farmers.objects.filter(state=request.POST['state'],crop2=request.POST['crop']))
        farmers.append(Farmers.objects.filter(state=request.POST['state'],crop3=request.POST['crop']))
        farmers.append(Farmers.objects.filter(state=request.POST['state'],crop4=request.POST['crop']))
        farmers.append(Farmers.objects.filter(state=request.POST['state'],crop5=request.POST['crop']))
        print(farmers)
        
        return render(request,'rate.html',{'farmers':farmers})

def farmer_insert(request):

    if(request.POST['password']==request.POST['Cpassword']):

        if not Farmers.objects.filter(username=request.POST['username']).exists():
            farmer = Farmers()
            farmer.first_name = request.POST['farmer_first_name']
            farmer.last_name = request.POST['farmer_last_name']
            farmer.crop1 = request.POST['crop1']
            farmer.crop2 = request.POST['crop2']
            farmer.crop3 = request.POST['crop3']
            farmer.crop4 = request.POST['crop4']
            farmer.crop5 = request.POST['crop5']
            farmer.state = request.POST['state']
            farmer.contact = request.POST['contact']
            farmer.username = request.POST['username']
            farmer.password =pbkdf2_sha256.encrypt(request.POST['password'],rounds=1,salt_size=0)
            farmer.save()
            return redirect('farmerLogin')
        else:
            messages.info(request,'Username Already Present')
            return redirect('farmReg')
    else:
        messages.info(request,'Password Not Matching')
        return redirect('farmReg')

def farmerLogin(request):
    if request.method == 'POST':
        if Farmers.objects.filter(username=request.POST['username'],password=pbkdf2_sha256.encrypt(request.POST['password'],rounds=1,salt_size=0)).exists():
            return redirect('farmerLogin/getRate')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'farmerLogin.html')

    else:
        return render(request,'farmerLogin.html')

def customerReg(request):
    return render(request,'customerReg.html')

def customer_insert(request):
    if(request.POST['password']==request.POST['Cpassword']):

        if not Customers.objects.filter(username=request.POST['username']).exists():
            customer = Customers()
            customer.first_name = request.POST['customer_first_name']
            customer.last_name = request.POST['customer_last_name']
            customer.state = request.POST['state']
            customer.contact = request.POST['contact']
            customer.username = request.POST['username']
            customer.password =pbkdf2_sha256.encrypt(request.POST['password'],rounds=1,salt_size=0)
            customer.save()
            return redirect('customerLogin')
        else:
            messages.info(request,'Username Already Present')
            return redirect('customerReg')
    else:
        messages.info(request,'Password Not Matching')
        return redirect('customerReg')

def customerLogin(request):
    if request.method == 'POST':
        if Customers.objects.filter(username=request.POST['username'],password=pbkdf2_sha256.encrypt(request.POST['password'],rounds=1,salt_size=0)).exists():
            return redirect('customerLogin/getRate')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'customerLogin.html')
    else:
        return render(request,'customerLogin.html')
