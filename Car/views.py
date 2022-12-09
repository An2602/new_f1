from django.http import HttpResponse
from django.shortcuts import render
from Car.models import Car

def list_of_cars(request):
    mycars= Car.objects.all()
    context = {
        'cars_list': mycars,
    }
    return render(request, 'cars.html', context=context)