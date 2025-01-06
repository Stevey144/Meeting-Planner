from django.forms import modelform_factory
from django.shortcuts import redirect, render,get_object_or_404

from .models import Meeting, Room

from .forms import MeetingForm


def detail(request, id):
    meeting =get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms" : Room.objects.all()})

#<---! important -->
# MeetingForm = modelform_factory(Meeting, exclude=[])
# this is an auto generated python form using the meeting model class objects
#use this if you dont want to set the attribute for the form manually, you just want python model class to do the magic!

#<---! important -->

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the meeting to the database
            return redirect('welcome')  # Adjust this URL as needed
    else:
        form = MeetingForm()  # Render an empty form for GET requests

    return render(request, "meetings/new.html", {"form": form})