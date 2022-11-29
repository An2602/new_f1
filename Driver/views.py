from django.http import HttpResponse
from django.template import loader
from Driver.models import Driver
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="mylogin")
def list_of_drivers(request):
    mydrivers= Driver.objects.all()
    context = {
        'driver_list': mydrivers,
    }
    return render(request, 'drivers.html', context=context)

# @login_required(login_url="mylogin")
def homepage(request):
    return render(request, 'index.html')

def single_driver(request, pk):
    driver = Driver.objects.get(id=pk)
    return render(request, 'single_driver.html', {'driver':driver})

def edit_driver(request, pk):
    driver = Driver.objects.get(id=pk)
    if request.method == "GET":
        return render(request, 'edit_driver.html', {'driver':driver})
    
    driver.name = request.POST.get('name')
    driver.score = request.POST.get('score')
    driver.save()
    messages.info(request, "SAVED SUCCSSEFULY")
    return render(request, 'single_driver.html', {'driver':driver})

def delete_driver(request, pk):
    driver = Driver.objects.get(id=pk)
    driver.delete()
    return redirect('Driver:Driver')

@login_required(login_url="mylogin")
def driver_standing(request):
    all_drivers= Driver.objects.all().order_by('-score').values()
    context = {
        'driver_standing': all_drivers,
    }
    return render(request, 'standing.html', context=context)

