from django.shortcuts import render

# Create your views here.
def layouthome(request):
    return render(request,"layoutdemo/Home.html")

def layoutaboutus(request):
    return render(request,"layoutdemo/AboutUS.html")

def layoutContactUs(request):
    return render(request,"layoutdemo/ContactUs.html")
