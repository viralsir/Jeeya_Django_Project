from django.urls import path
from .views import greetings,welcome,aboutus,contactus

urlpatterns = [

    path('greeting/',greetings),  # hello/greeting
    path('welcome/',welcome),
    path('about/',aboutus),
    path('contact/', contactus)
]