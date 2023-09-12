""" 
    Ativar ambiente virtual 
        Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
        python -m venv venv
        .\venv\Scripts\Activate.ps1

    Desativando o ambiente virtual
        deactivate

    Iniciando um projeto com o django
        django-admin startproject <nome do projeto> .(raiz)

    Iniciando o server django
        python manage.py runserver

    O "manage.py" 
"""