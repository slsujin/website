from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username= request.POST['Username']
        firstname= request.POST['First_name']
        lastname= request.POST['Last_name']
        email= request.POST['Email']
        password= request.POST['Password']
        cpassword= request.POST['Password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email)
                user.save();
                print("user registered")
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
            print("password not matching")
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


