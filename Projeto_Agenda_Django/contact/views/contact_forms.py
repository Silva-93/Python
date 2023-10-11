# type: ignore
from django.shortcuts import get_object_or_404, render, redirect  
from django.db.models import Q 
from contact.models import Contact
from django.core.paginator import Paginator 
from django import forms


# Criando um formulário com Django
class ContactForm(forms.ModelForm):
    class Meta:
        model: Contact  # Indicando o formulário

        # indicando os campos que serão utilizados
        fields = ('first_name', 'last_name', 'phone',)

# Create your views here.
def create(request):


    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )