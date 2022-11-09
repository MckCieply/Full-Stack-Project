from django.shortcuts import render
from django.http import HttpResponse
from .models import Cars
# Create your views here.

def index(response):
    return render(response, "cardeals/base.html", {})

def home(response):
    return render(response, "cardeals/home.html", {})

def roccodeals(response):
    return render(response, "cardeals/rocco.html", {})

def lancerdeals(response):
    return render(response, "cardeals/lancer.html", {})