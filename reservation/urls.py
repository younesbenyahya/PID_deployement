
from django import views
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home, name="home"),
    #path('login',login, name="login"),
    path('register',register, name="register"),
    path('addandshow',addandshow, name="addandshow"),
]
