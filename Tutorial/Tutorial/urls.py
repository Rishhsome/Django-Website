"""Tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Manually Added to modify the admin site
admin.site.site_header = "RISHABH Ice Cream Admin"
admin.site.site_title = "RISHABH Ice Cream Admin Portal"
admin.site.index_title = "Welcome to RISHABH Ice Cream"

urlpatterns = [
    path('admin/', admin.site.urls), #This will run when we use 127.0.0.1:8000/admin/ which will redirect us to an admin page provided by django
    path('', include('MyAppTrial.urls'))  # This will run when we use 127.0.0.1:8000/ and it will direct it to urls.py of MyAppTrial
]


# urlpatterns += staticfiles_urlpatterns()
