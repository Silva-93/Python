'''
    Iterável -> str, range, etc (__iter__)
    Iterador -> quem sabe entrergar um valor por vez
    next -> entregue-me o próximo valor
    iter -> entregue-me seu iterador
'''

# texto = 'Python'

# novoTexto = ''
# for letra in texto:
#     novoTexto += f'*{letra}'
#     print(letra)

# print(novoTexto)



# função range(início, fim, passo)

# numeros = range(0, 10, 2)  #  Indo do 0 ao 10 pulando de 2 em 2

# for numero in numeros:
#     print(numero)




#texto = iter('texto')  # __iter__()

#print(texto)
# print(texto.__next__())  #  entregando um elemento da variável "texto" por vez
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

#  outra maneira

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))



# for i in range(1, 10):
#     if i == 2:
#         print('i é igual a 2, pulando...')
#         continue
    
#     if i == 8:
#         print('i é igual a 8, seu else não será executado')
#         break

#     for j in range(1, 3):
#         print(i, j)
# else:
#     print('for completo com sucesso!')
    


#  Exercício
'''
    Faça um jogo para o usuário adivinhar a palavra secreta.
    Você vai propor uma palavra secreta qualquer e vaidar a 
    possibilidade do usuário digitar apenas uma letra.

    Quando o usuário digitar a letra você var conferir se a 
    letra está dentro da paralavra secreta.

    Se a letra digitada estiver na palavra secreta, exiba a letra

    Se a letra não estiver na palavra secreta, exiba *

    Faça uma contagem das tentativas do usuário.
'''


palavra_secreta = 'secreta'
letras_acertadas = ''
numero_tentativas = 0


while True:
    letra_digitada = input('Digite uma letra para adivinha a palavra secreta.\nLetra: ')
    numero_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada  # armazenando as letras acertadas

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'
    

    print(f'Palavra formada: "{palavra_formada}"')


    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU! PARABÉNS!')
        print(f'A palavra era "{palavra_secreta}"')
        print(f'O número de tentativas foram {numero_tentativas}')
        break











