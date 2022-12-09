from django.urls import path
from . import views
 
urlpatterns = [
   path('all_Cars/', views.list_of_cars),
]