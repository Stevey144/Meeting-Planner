from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",{"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("The page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("I am Stephen Ogechi, a software engineer with in-depth experience of Api Integration")
