from django.contrib import admin
from django.urls import path
from MyAppTrial import views

urlpatterns = [
    path('admin/', admin.site.urls),  #This will run when we use 127.0.0.1:8000/admin/ which will redirect us to an admin page provided by django
    path('', views.index, name='home'),  #This will run when we use 127.0.0.1:8000/ and it will redirect it to views.py of MyAppTrial
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]