'''
    Dicionários são estrutura de dados de par "chave" e "valor".
    Chaves pode ser con siderada com "índice" que vimos em listas e podem ser do tipo "imutáveis" como: str, int, float, bool, tuple etc.
    O valor pode ser qualqer tipo, incluindo outro dicionário.
    Usamos as chaves - {} - ou a class dict() para criar dicionários.
    
    Imutáveis: str, int, float, bool, tuple

    Mutáveis: dict(), list()
'''

#  Criando um dicionário
#             chave  valor
# pessoa2 = dict(nome='José')
# print(pessoa2)

# outra maneira de fazer um dicionário e a maneira mais utilizada

# pessoa = {
# #   chave: valor
#     'nome': 'Jouber',
#     'sobrenome': 'Vicente',
#     'idade': 29,
#     'altura': 1.75,
#     'endereços': [
#         {'rua': 'Nova Jales', 'número': 600},
#         {'Av': 'Sebastião Salazar', 'número': 600}
#     ]
# }
# print(pessoa)

# Acessando valores do dicionário
# print(pessoa['nome'])
# print(pessoa['idade'])
# print(pessoa['endereços'])


# # Outra maneira de acessar os valores dos dicionários
# for chave in pessoa:  # Acessando todas as chaves do dicionário
#     print(chave)


# for chave in pessoa:  # Acessando todas as chaves e valores do dicionário
#     print(chave, pessoa[chave])


# Manipulando as chaves e valores dos dicionários
# pessoa = {}

# # Criando uma chave:valor no dicionário
# pessoa['nome'] = 'Fulano'

# print(pessoa)

# #  Alterando os valores da chave

# pessoa['nome'] = 'Sicrano'
# print(pessoa)

# #  Apagando uma chave
# pessoa['sobrenome'] = 'Beltrano'
# print(pessoa)

# del pessoa['sobrenome']
# print(pessoa)

# #  Verificando se uma chave existe

# if pessoa.get('sobrenome') is None:
#     print('Chave não existente.')
# else:
#     print(pessoa['sobrenome'])


'''
    Métodos úteis nos dicionários

    len - Quantidade de chaves
    keys - Iterável com as chaves
    values - Iterável com os valores
    items - Iterável com as chaves e valores
    setdefault - Adiciona valores se a chave não existir
    copy - Retorna ums cópia rasa (shallow copy)
    get - Obtem uma chave
    pop - Apaga um item com a chave especificada (del)
    popitem - Apaga o último item adicionado
    update - Atualiza o dicionário com outro, pode alterar o valor de uma chave, altera uma chave e adicionar novas chaves:valores
'''


# pessoa = {
# #   chave:   valor
#     'nome': 'Jouber',
#     'sobrenome': 'Vicente',
#     'altura': 1.75,
# }

# print(len(pessoa))  # número de chaves no dicionário


# print(pessoa.keys())  # pegando as chaves
# # outra maneira de pegar as chaves
# for chave in pessoa.keys():
#     print(chave)


# print(pessoa.values())  # pegando os valores
# # outra maneira de pegar os valores
# for valores in pessoa.values():
#     print(valores)


# print(pessoa.items())  # pegando as chaves e valores
# # Outra maneira
# for chave, valor in pessoa.items():
#     print(f'{chave}: {valor}')



# pessoa.setdefault('idade', 29)  # adciona uma chave:valor caso ele não exista
# print(pessoa['idade'])

# from copy import deepcopy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'c3': 3
# }

# d2 = d1.copy()  # Cria uma cópia de todos os valores imutáveis da lista, quando a um elemento com valores mutáveis, o ".copy()" aponta esse elemento para o mesmo local na memória do dicionário original.

# d2['c1'] = 100

# print(d1)
# print(d2)


# #  Para fazer uma cópia completa do dicionário é preciso importa o módulo 'copy' e usa o método 'deepcopy()'

# d2 = deepcopy(d1)  # cópia completa




p1 = {
    'nome': 'Jouber',
    'sobrenome': 'Vicente'
}

# print(p1.get('nome'))  # Obtem o valor de uma chave, por padrão o valor retornado é 'None'


# nome = p1.pop('nome')  # Apaga um item com a chave especificada mas guardando o valor do mesmo
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()  # Apaga último item do dicionário guardando o valor do mesmo
# print(ultima_chave)
# print(p1)




#  Atualizando os valores do dicionário e adicionando mais chaves:valores.
# p1.update({
#     'nome': 'Fulano',
#     'sobrenome': 'Beltrano',
#     'idade': 100 
# })

# Outra maneira de atualizar
# p1.update(nome='Fulano', sobrenome='Beltrano', idade=100)

# print(p1)




# Exercício 
# Sistema de pergunta e resposta

perguntas = [
    {
        'Pergunta': 'Quando é 2 + 2',
        'Opções': ['1', '2', '3', '4'],
        'Resposta': '4'
    },
    
    {
        'Pergunta': 'Quando é 5 * 5',
        'Opções': ['55', '20', '25', '10'],
        'Resposta': '25'
    },

    {
        'Pergunta': 'Quando é 10 / 2',
        'Opções': ['5', '2', '3', '4'],
        'Resposta': '5'
    },
]

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    
    escolha = input('Escolha uma opção: ')
    escolha_int = None
    qtd_opcoes = len(opcoes)
    acertou = False
    qtd_acertos = 0

    # Checando se o que foi difitado é um digito (número)
    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True



    if acertou:
        qtd_acertos += 1
        print('\033[32mAcertou!\033[0;0m')
    else:
        print('\033[31mErrou!\033[0;0m')
























