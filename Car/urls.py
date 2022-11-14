from django.urls import path
from . import views
 
urlpatterns = [
   path('all_Cars/', views.Car),
]