from django.shortcuts import render, redirect  # type: ignore
from contact.forms import ContactForm
from django.urls import reverse  #type: ignore

def create(request):
    form_action = reverse('contact:create')


    if request.method == 'POST':
        form = ContactForm(request.POST)  # Dados do formulário

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

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