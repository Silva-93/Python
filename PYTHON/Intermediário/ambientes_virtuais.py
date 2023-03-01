"""
    Ambientes virtuais em Python (venv)

    Um ambiente virtual carrega toda a sua instalação  do Python para uma pasta no caminho escolhido.

    Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.

    venv é o módulo que vamos usar para  criar ambientes virtuais.

    Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são:
    venv env .venv .env
"""

""" 
    Criando um ambiente virtual no Windows no Power Shell

    python -m venv <nome> 
"""

""" 
    gcm <executavel>      Mostra o local onde o executável está

    gcm python

    ou

    gcm python -Syntax

    C:\Users\Jouber\AppData\Local\Programs\Python\Python311\python.exe
"""

""" 
    Permitindo o ambiente virtual pelo power shell

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
"""

"""
    Ativando o ambiente virtual

    .\venv\Scripts\actvate

    para desativar digite "deactivate
"""

"""
    pip freeze -> mostra os pacotes instalados
"""

"""
    Criando um arquivo de configuração para instalações futuras

    pip freeze > requirements.txt

    Para instalar os programas nas versões que estão no arquivo "requirements.txt"

    pip install -r .\requirements.txt
"""

