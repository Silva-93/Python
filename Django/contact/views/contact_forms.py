from django.shortcuts import render, get_object_or_404, redirect  # type: ignore
from django.db.models import Q  # type: ignore
from contact.models import Contact
from django.core.paginator import Paginator  # type: ignore
from django import forms  # type: ignore


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Modelo para criação do formulário
        fields = 'first_name', 'last_name', 'phone',  # campos do formulário


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)  # Dados do formulário
        }

        return render(
            request,
            'contact/create.html',
            context
        )        

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )