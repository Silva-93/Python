from django.contrib import admin  # type: ignore
from . import views  
from django.urls import path, include  # type: ignore

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),  # type: ignore
] 