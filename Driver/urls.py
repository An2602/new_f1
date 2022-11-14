from django.urls import path
from . import views

app_name="Driver"

urlpatterns = [
   path('', views.list_of_drivers, name="Driver"),
   path('all_drivers/', views.list_of_drivers),
   path('<pk>/', views.single_driver, name="single"),
   path('<pk>/edit', views.edit_driver, name="edit"),
   path('<pk>/delete', views.delete_driver, name="delete")
]