from django.urls import  path
from .views import *

urlpatterns = [
        path("home/",Home,name='student-home'),
        path("about/",aboutus,name='student-aboutus'),
        path("contactus/",contactus,name='student-contactus')
]
