from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        a=request.POST['username']
        d=request.POST['password']
        x=auth.authenticate(username=a,password=d)

        if x is not None:
            auth.login(request,x)
            return redirect('/')

        else:
            messages.info(request,"invalid creditentials")
            return redirect('login')

    return render (request,'login.html')

def register(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['last_name']
        c = request.POST['email']
        d = request.POST['password']
        e = request.POST['password_2']
        if d == e:
            if User.objects.filter(username=a).exists():
                messages.info(request,"username already exists")
                return redirect('register')

            if User.objects.filter(email=c).exists():
                messages.info(request,"email already exists")
                return redirect('register')




            x = User.objects.create_user(username=a,
                                     last_name=b,
                                     email=c,
                                     password=d)
            x.save();

        else:
            messages.info(request,"password not matching")

        return redirect('login')

    return render(request, "register.html")
