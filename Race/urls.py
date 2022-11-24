from django.urls import path
from . import views
 
urlpatterns = [
   path('all_races/', views.standing_in_races),
]
