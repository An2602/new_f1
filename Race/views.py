from django.http import HttpResponse
from django.shortcuts import render, redirect
from Driver.models import Driver
from Race.models import Race, Standing_in_race
from Race.forms import RaceForm, StandingForm
from Race.models import Standing_in_race
from django.contrib.auth.decorators import login_required
 
@login_required(login_url="mylogin")
def standing_in_races(request):
    standing_by_race= Standing_in_race.objects.all()
    context = {
        'standing_list': standing_by_race,
    }
    return render(request, 'races.html', context=context)


# @login_required(login_url="mylogin")
# def standing_in_races(request):
#     races= Race.objects.all()
#     context = {
#         'races': races,
#     }
#     return render(request, 'races.html', context=context)

def update_fast_driver_score(standing):
    race_type = standing.race_type
    fastest_driver = standing.fastest_driver
    if race_type == Race.Race_type.regular:
        fastest_driver.score += 1
        fastest_driver.save()


def add_race(request):
    context = {
        'raceform': RaceForm(),
    }
    return render(request, 'addrace.html', context)


def add_race_action(request):
    raceform = RaceForm(request.POST, request.FILES)
    if raceform.is_valid():
        standing = raceform.save()
        update_fast_driver_score(standing)
        return redirect('races:races')
    else:
        context = {
            'raceform': raceform,
        }
        return render(request, 'addrace.html', context)

    

def update_driver_score(standing):
    regular_dic = {1:25, 2:18, 3:15, 4:12, 5:10, 6:8, 7:6, 8:4, 9:2, 10:1}
    sprint_dic = {0:8, 1:7, 2:6, 3:5, 4:4, 5:3, 6:2, 7:1}
    driver = standing.driver
    race = standing.race
    if race.race_type == Race.Race_type.regular:
        driver.score += regular_dic.get(standing.standing)
    elif race.race_type == Race.Race_type.sprint:
        driver.score += sprint_dic.get(standing.standing)
    driver.save()       
        
def add_standings(request):
    context = {
        'standingform': StandingForm(),
    }
    return render(request, 'addstandings.html', context)

def add_standings_action(request):
    standingform = StandingForm(request.POST, request.FILES)
    if standingform.is_valid():
        standing = standingform.save()
        update_driver_score(standing)
        return redirect('races:races')
    else:
        context = {
            'standingform': standingform,
        }
        return render(request, 'addstandings.html', context)





# def get_race_standing(request, pk):
#     race = Race.objects.get(id=pk)
#     drivers = Driver.objects.all()
#     return render(request,{'race':race,'drivers':drivers})

# def save_race_standing(request,pk):
#     race = Race.objects.get(id=pk)
#     save_standing(request, "firstplace")
#     save_standing(request, "secondplace")
#     save_standing(request, "thirdplace")
#     save_standing(request, "fourthplace")
    

# def save_standing(place, request, race):
#     number1=request.POST.get("cars1")
#     driver = Driver.get(id=number1)
#     standing = Standing_in_race(race=race,driver=driver)
#     standing.save()


    



