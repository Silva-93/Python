from django.shortcuts import render, redirect  # type: ignore
from django.contrib import messages, auth  # type: ignore
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm  # type: ignore

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


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)  # autenticação do login
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')
        
        messages.error(request, 'Login inválido.')
            
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')