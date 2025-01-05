from django.forms import modelform_factory
from django.shortcuts import render

from .models import Meeting, Room


def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms" : Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
