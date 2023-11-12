""" 
    Fala um program que leia o nome completo e mostre
        O nome com todas as letras maiúsculas
        O nome com todas as letras minúsculas
        A quantidade de letras que o nome tem (sem os espaços)
        Quantas letras o primeiro nome tem  
"""

nome = str(input('Digite seu nome completo.\nNome: ')).strip()  # tira os espaços do começo e final

nome_maiusc = nome.upper()
nome_minusc = nome.lower()
tamanho_nome = len(nome.replace(' ', ''))  # tirando todos os espaços
tamanho_primeiro_nome = len(nome[0:6])

print(f'Seu nome em letras maiúscula é: {nome_maiusc}')
print(f'Seu nome em letras minúculas é: {nome_minusc}')
print(f'Seu nome tem: {tamanho_nome} letras')
print(f'Seu Primeiro nome tem {tamanho_primeiro_nome} letras')
