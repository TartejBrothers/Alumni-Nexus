from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template import loader
from .form import add_data
from .models import Alumni

# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "home.html")


def signup(request):
    form = add_data(request.POST or None)
    if form.is_valid():
        form.save()
        form = add_data()
    dict5 = {"form": form}
    return render(request, "signup.html", dict5)


def items(request):
    alumni = Alumni.objects.all()
    return render(request, "details.html", {"alumni": alumni})
