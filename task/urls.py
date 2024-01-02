from django.urls import path
from .views import *
urlpatterns=[
        path("",home,name="task-view"),
        path("add/",addTask,name="task-new")

]