
"""
URL configuration for meeting_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from meetings import views
from website.views import welcome
from website.views import date
from website.views import about
from meetings.views import detail

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('welcome.html',welcome, name="welcome"),
    path('',welcome),
    path('date',date),
    path('about',about),
    #use line 34 to include relevant links from other route instead of 32 and 33
    # path('meetings/<int:id>', detail, name="detail"),
    # path('rooms', rooms_list, name="rooms"),
    path('meetings/', include('meetings.urls'))
    
    
]
