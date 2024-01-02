from django.shortcuts import render,redirect

# Create your views here.
tasklist=["pay electricity bill","do homework","recharge mobile","repair laptop"]

def home(request):
    return render(request,"task/viewtask.html",{
        "tasklist":tasklist
    })

def addTask(request):

    if request.method=='POST':
           print(request.POST["task"])
           tasklist.append(request.POST["task"])
           return redirect("task-view")

    return render(request,"task/addtask.html")
