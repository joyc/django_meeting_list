from django.shortcuts import render, redirect, get_object_or_404

from .models import Meeting, Room
from .forms import MeetingForm


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


# add page of all room list
# - view / template / url mapping
def room_list(request):
    return render(request, "meetings/room_list.html",
                  {"rooms": Room.objects.all()})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})