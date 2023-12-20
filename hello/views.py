from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greetings(request):
    return HttpResponse("<h1>hello how are you ? </h1>");

def welcome(request):
    return HttpResponse("<h1 style='color:red'>wel come to the world of Django </h1>");

def aboutus(request):
    return HttpResponse("<h3> this is a aboutus page </h3>")

def contactus(request):
    return HttpResponse("<h3> this is a contactus page </h3>")
