from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "detail.html", {"meeting": meeting})


# add page of all room list
# - view / template / url mapping
def room_list(request):
    return render(request, "room_list.html",
                  {"rooms": Room.objects.all()})

