from django.urls import include, path

from django.contrib import admin

from .import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.rooms_list, name="rooms"),
    path('new', views.new, name="new"),
]

