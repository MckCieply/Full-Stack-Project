from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h2> Car deals </h2>")

def roccodeals(response):
    return HttpResponse("<h5> Rocco Deals </h5>")

def lancerdeals(response):
    return HttpResponse("<h5> Lancer Deals </h5>")