from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This data was  sent from the view to the template.",
                   "x": "3.0.5"})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("This is a about page.")