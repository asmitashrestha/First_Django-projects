from os import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import features
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username, password=password, email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password is not same')
            return redirect('register')    
    return render(request,'register.html')

def counter(request):
    text =request.GET['text']
    amountofwords =len(text.split())
    return render(request,'counter.html',{'amount':amountofwords})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
 
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Credential Invalid')
            return redirect('login')
    else:
        return render(request,'login.html') 
def logout(request):
    auth.logout(request)
    return redirect('/')
