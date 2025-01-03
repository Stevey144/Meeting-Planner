from django.urls import path
from .import views

ulrpatterns =[
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.rooms_list, name="rooms")
    
]

