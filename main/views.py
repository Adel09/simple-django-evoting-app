from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main/login.html')
    else:
        username = request.POST['matnumber']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard-home')
        else:
            context = {
                'message' : "Incorrect Password"
            }
            return render(request, 'main/login.html', context)

def registeruser(request):
    if request.method == 'GET':
        return render(request, 'main/register.html')
    else:
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        username = request.POST['matnumber']
        password = request.POST['password']
        try:
            user = User.objects.create_user(
                first_name=first_name, 
                last_name=last_name,
                username=username,
                email=email,
                password=password
                )
            user.save()
            login(request, user)
            return redirect('dashboard-home')
        except IntegrityError:
            context = {
                'message' : "User already exists"
            }
            return render(request, 'main/register.html', context)
