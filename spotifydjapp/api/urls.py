from django.urls import path
from .views import main

urlpatterns = [
    path('',main), # if we a blank url, call the 'main' function
    path('home',main)
]
