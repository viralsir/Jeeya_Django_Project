from django.urls import path
from .views import *
urlpatterns = [
    path('home/',layouthome,name="layout-home"),
    path('aboutus/',layoutaboutus,name="layout-aboutus"),
    path('contactus/',layoutContactUs,name="layout-contactus")
]