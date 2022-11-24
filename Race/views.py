from django.http import HttpResponse
from django.shortcuts import render
from Race.models import Standing_in_race
from django.contrib.auth.decorators import login_required
 
@login_required(login_url="mylogin")
def standing_in_races(request):
    standing_by_race= Standing_in_race.objects.all()
    context = {
        'standing_list': standing_by_race,
    }
    return render(request, 'races.html', context=context)

