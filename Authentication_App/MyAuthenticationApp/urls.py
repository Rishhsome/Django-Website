from django.contrib import admin
from django.urls import path, include
from MyAuthenticationApp import views

urlpatterns = [
    path('', views.index, name="MyAuthenticationApp"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout")
]