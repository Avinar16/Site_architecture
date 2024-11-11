
from django.contrib import admin
from django.urls import path
from api.views import get_joke

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', get_joke, name='get_joke')
]
