from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages,auth
# Create your views here.
from newwapp.models import Upload_ph, Details


def index(request):
    obj=Upload_ph.objects.all()
    obj1=Details.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})

def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'The user is already exist')
                return redirect('reg_ster')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'The email is already exist')
                return redirect('reg_ster')
            else:
                user=User.objects.create_user(username=uname,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                return redirect('log_in')
        else:
            messages.info(request,'password not matching')
            return redirect('reg_ster')
        return redirect('/')
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credential')
            return redirect('log_in')
    return render(request,'log_in.html')

def logout(request):
    auth.logout(request)
    return redirect('/')