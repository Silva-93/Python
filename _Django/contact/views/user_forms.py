from django.shortcuts import render, redirect  # type: ignore
from django.contrib import messages  # type: ignore
from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    # messages.info(request, 'Mensagem de INFORMAÇÃO.')
    # messages.warning(request, 'Mensagem de ATENÇÃO.')
    # messages.error(request, 'Mensagem de ERRO.')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado.')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
