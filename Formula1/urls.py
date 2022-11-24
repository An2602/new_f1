"""Formula1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from Driver.views import list_of_drivers,homepage
from . import settings
from django.contrib.auth.decorators import login_required
from Driver import mylogin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Car/', include('Car.urls')),
    path('Driver/', include('Driver.urls')),
    path('Race/', include('Race.urls')),
    path('',homepage),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', mylogin.mylogin, name='mylogin'),
    path('logout/', mylogin.mylogout, name='logout'),
    path('register/', mylogin.register, name='register'),
]
 
 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)