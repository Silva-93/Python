from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'phone',)  # Informa quis os campos que serão mostrados no list display
    ordering = '-id',  # ordena pelo id de forma decrescente
    # list_filter = 'create_date',  # cria um filtro pela data
    search_fields = 'id', 'first_name', 'last_name',  # adiciona um campo de pesquisa
    list_per_page = 1  # cria uma paginação
    list_max_show_all = 100  # mostra 100 contatos por página
    list_editable = 'first_name', 'last_name'  # adiciona uma forma de editar os valores sem ter que entrar no contato
    list_display_links = 'id',  # adiciona um link para entrar nas configurações do contato, campo não pode estar no list_editable e o campo deve estar referido no list_display