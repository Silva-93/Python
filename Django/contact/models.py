from django.db import models  # type: ignore
from django.utils import timezone  # type: ignore

# Create your models here.
class Contact(models.Model):
    # Criando campos da tabela
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
