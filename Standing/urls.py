from django.urls import path
from . import views
 
urlpatterns = [
   path('driver_standing/', views.Standing)
]
