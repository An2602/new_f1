from django.urls import path
from . import views

app_name = 'races'

urlpatterns = [
   path('all_races/', views.standing_in_races, name="races"),
   path('add_race/', views.add_race, name="add_race"),
   path('add_race_action/', views.add_race_action, name="add_race_action"),
   path('add_standings/', views.add_standings, name="add_standings"),
   path('add_standings_action/', views.add_standings_action, name="add_standings_action"),

]
