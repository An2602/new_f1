from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def mylogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:    
            User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist.')
            return render(request, 'login.html', {})

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Driver:Driver')
        else:
            messages.error(request, 'Password not correct.')

    return render(request, 'login.html', {})

def mylogout(request):
    logout(request)
    return render(request, 'index.html', {})

def register(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'register.html' ,{'form':form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Driver:Driver')
        messages.error(request, 'Failed to register, Please try again')    
        return render(request, 'register.html',{'form':form})