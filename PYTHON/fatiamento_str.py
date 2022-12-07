

'''
    fatiamento[inicio:fim:passo]
'''

variavel = 'Olá mundo!'

print(variavel[5])  #  Retorna o caracter no indice 5
print(variavel[-1])  #  Retorna o último caracter da str
print(variavel[4:])  #  Retorna a str do índice 4 até o final
print(variavel[:-6])  #  
print(variavel[0::2])  #  Vai do início até o fim pulando de 2 em 2 caracteres
print(variavel[::-1])  #  Inverte a str
print(len(variavel))  #  Retorna a quantidade de caractares da variável


#  Exercício

nome = input('Digite seu nome.\nNome: ')
idade = input('Digite sua idade.\nIdade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome {nome} contém espaços')
    else:
        print(f'Seu nome {nome} não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')









