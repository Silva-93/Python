from django.contrib import admin  # type: ignore
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin): 
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = 'id',  # ordena pelo id, caso coloque o sinal de “-“(‘-id’) vai ordena de forma decrescente.
    # list_filter = 'created_date',  # cria um filtro de data
    search_fields = 'id', 'first_name', 'last_name',  # cria um campo de busca
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name', 
    list_display_links = 'id',