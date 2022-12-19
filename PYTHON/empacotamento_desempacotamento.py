'''
    Introdução ao desempacotamento
'''



#  nomes empacotados
# listaNome = ['Joao', 'Maria', 'Suzana']

#  atribuindo os nomes da lista a cada variável "desempacotando"
# nome1, nome2, nome3 = listaNome
# print(nome2)


#  Como há poucas variáveis para a quantidade de valores na lista. as variáveis "nome1" e "nome2" vão pegar os 2 primeiros valores da lista e o resto dos valors serão empacotados em outra variável chamda "resto"
nome1, nome2, *resto = ['Joao', 'Maria', 'Suzana', 'Vitor', 'Ana']  
print(nome1)
print(resto)

#  O primeiro valor será ignorado e a variável "nome2" só pegará o segundo valor da lista. O resto também será ignorado
_, nome2, *_= ['Joao', 'Maria', 'Suzana', 'Vitor', 'Ana']
print(nome2)



















