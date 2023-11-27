from django.contrib import admin  # type: ignore
from . import views  
from django.urls import path, include  # type: ignore

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),  # type: ignore
    path('', views.index, name='index'),  # type: ignore
    
    # contact (CRUD)
    path('contact/create/', views.create, name='create'),  # type: ignore
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),  # type: ignore
] 