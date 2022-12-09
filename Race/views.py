from django.http import HttpResponse
from django.shortcuts import render, redirect
from Race.models import Race, Standing_in_race
from Race.forms import RaceForm, StandingForm
from Race.models import Standing_in_race
from django.contrib.auth.decorators import login_required


@login_required(login_url="mylogin")
def standing_in_races(request):
    races = {}
    st = Standing_in_race.objects.all().order_by('standing')
    for standing in st:
        if not races.get(standing.race_id):
            races[standing.race_id] = [standing.race]
        races[standing.race_id].append(standing)
    return render(request, "races.html", {'races':races.values()})
    


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
    sprint_dic = {1:8, 2:7, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1}
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

    



