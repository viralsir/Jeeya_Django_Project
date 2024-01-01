from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):

    return render(request,"newyear/home.html",{
        "msg":"hello",
        "name":"vimal",
        "newyear": datetime.utcnow().month==1 and datetime.utcnow().day==1
    })