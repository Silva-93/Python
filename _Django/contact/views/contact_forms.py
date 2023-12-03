from django.shortcuts import render  # type: ignore
from contact.forms import ContactForm

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