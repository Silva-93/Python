from django.contrib import admin  # type: ignore
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin): 
    ...