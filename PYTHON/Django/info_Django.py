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

    No arquivo "settings.py" é onde vai ser configurado tudo sobre o projeto.

    O arquivo "urls.py" é a mão de todas as urls do seu programa. Só existe na raiz do projeto, inicialmente

    O arquivo "wsgi.py" é a interface de comunicação do django com o servidor que estiver sendo utilizado.

    Iniciando um app (aplicação)
        python manage.py startapp <nome da aplicação> -> Esse comando irá criar um diretório com o nome do app onde vão ficar as configurações dessa aplicação. Que terá os arquivos "admin.py, apps.py, models.py, tests.py, views.py"
    
    O arquivo "admin.py" que é a página de administração. É onde serão registrados os models do projeto.

    O arquivo "apps.py", esse é o arquivo onde ficarão as configurações da aplicação.

    O arquivo "models.py", é onde serão criados os models.

    O arquivo "views.py", é onde serão criadas as views. 


    Para configurar uma página html no djando é necessário configurar as views com o arquivo html e indicalos nas settings.py do projeto em INSTALLED_APPS. Dentro do app crie uma pasta com o nome "templates" e dentro dessa pasta crie outra pasta com o nome do app, nela é onde ficarão os arquivos html.

    Templates globais -> No arquivo "settings.py" do projeto há uma variável chamada "TEMPLATES", nela, há um chave chamada "'DIRS: []'" nela pode colocar diretórios onde se quer buscar templates.

    Partials -> São partes de códigos em um arquivo que pode ser utilizado em outro arquivo.

    Arquivos estáticos -> Por convenção é criado um diretório dentro dos apps nomeado "static", nele também é criado um diretório com o nome do app e dentro deste outros diretórios com os arquivos que serão utilizados, js, css, img etc. Dentro do partial html, na primeira linha digite {% load static %}, isso carregará os arquivos estáticos. No link que carrega os arquivos css coloque {% static '' %}, nele é onde será lincado o arquivo css

    Para enviar dados(text html) dinamicamente com o Djando, dentro do arquio "views.py" no 3° parâmetro da função "render()" usa um dicionário informando a chave e o valor. Dentro do template onde estão as extenções e blocos do Django, use "{{ chave }}" dentro do {% block %}{% block %} para "printar" o texto dejesado
        {% block %}
            {{ "chave" }}
        {% endblock %}
"""