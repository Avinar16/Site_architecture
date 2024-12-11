"""
URL configuration for factory project.

The `urlpatterns` list routes URLs to classes. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function classes
    1. Add an import:  from my_app import classes
    2. Add a URL to urlpatterns:  path('', classes.home, name='home')
Class-based classes
    1. Add an import:  from other_app.classes import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manipulator/', include('manipulator.urls'))
]
