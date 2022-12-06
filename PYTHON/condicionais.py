'''
    São usada para impor condições no código, esperando uma ação para serem executados.
    Leitura -> Se ... acontecer execute o código
               Se ... não acontecer execute o outro código

    if   /   elif   /  else
    se   se não se    se não
'''

# entrar = input('Você quer "entrar" ou "sair" ? ')


# if entrar == 'entrar':
#     print('Entrou')

# elif entrar == 'sair':
#     print('Saiu.')

# else:
#     print('Digite "entrar" ou "sair".')





#  EXERCÍCIO

n1 = int(input('Digite um número.\nNúmero 1: '))
n2 = int(input('Digite outro número.\nNúmero 2: '))


if n1 > n2:
    print(f'O primeiro número {n1=} é maior que o segundo número {n2=}')

elif n1 == n2:
    print(f'O valores de {n1=} e {n2=} são iguais')

else:
    print(f'O segundo número {n2=} é maior que o primeiro número {n1=}')




















