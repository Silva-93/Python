from django.db import models
from django.utils import timezone

# Create your models here.
""" 
    Campos da base de dados
    id (primary key - automático)
    first_name (string)
    last_name (string)
    phone (string)
    email (email)
    created_date (date)
    description (text)
    category (foreign key)
    show (boolean)
    owner (foreign key)
    pecture (image)
"""

# Criando a "tabela", sevira para criar, buscar, atualizar e deletar contatos da base de dados. Vai ser gerado uma nome "migração" para ser inserido na base de dados
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)  # "blank=True" torna o campo opcional
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) 
    show = models.BooleanField(default=True)  # assim que o contato for cadastrado ele será mostrado na tela
    picture =models.ImageField(blank=True, upload_to='pectures/%Y/%m/')


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'