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

    O arquivo "urls.py" é a mãe de todas as urls do seu programa. Só existe na raiz do projeto, inicialmente

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

    URLs -> Caso for trabalhar com urls no django, não é recomendado utilizar-las diretamente(hard code), em vez disso, é usando a sintaxe do django <a href="{% url '' %}">. Dentro do arquivo "urls.py" do app adicione o nome da url ↓
        urlpatterns = [
            path('', home_views.home, name='home'),  # Página HOME
        ]

    URLs dinâmicas -> 

    Cada alteração que é feita nos models, você está trabalhando na base de dados.

    Executando as migrations
        python manage.py migrate 
    Com esse comando é possível acesse a área "admin" do django "127.0.0.1/8000/admin"

    Criando um super usuário
        python manage.py createsuperuser
            name: <user>
            email: <e-amil>
            password: <passwd>
            password (again): <passwd>
    
    Mudando a senha do usuário
        python manage.py changepassword <user>

    
    Models -> Sempre que um models for modificado é necessário executar os comandos 
        python manage.py makemigrations
        python manage.py migrate

    Acessando o shell do django
        python manage.py shell
"""