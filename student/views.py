from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    #return HttpResponse("<h1> Student Home Page</h1>")
    return render(request,"student\Home.html")

def aboutus(request):
    return render(request,"student/aboutus.html")

def contactus(request):
    return render(request,"student/Contactus.html")
