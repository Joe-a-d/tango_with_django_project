from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    link =  "<a href='/rango/about/'>About</a><br>"
    return HttpResponse("Rango says hey there partner! \n" + link)

def about(request):
    link = "<a href='/rango/'>Index</a><br>"
    return HttpResponse("Rango says here is the about page. \n" + link)
