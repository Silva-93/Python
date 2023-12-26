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
    path('contact/<int:contact_id>/update/', views.update, name='update'),  # type: ignore
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),  # type: ignore
    
    # user (Create, Read, Update)
    path('user/create/', views.register, name='register'),  # type: ignore
    
] 