'''
    São usada para impor condições no código, esperando uma ação para serem executados.
    Leitura -> Se ... acontecer execute o código
               Se ... não acontecer execute o outro código

    if   /   elif   /  else
    se   se não se    se não
'''

entrar = input('Você quer "entrar" ou "sair" ? ')

if entrar == 'entrar':
    print('Entrou')

elif entrar == 'sair':
    print('Saiu.')

else:
    print('Digite "entrar" ou "sair".')





#  EXERCÍCIOS

n1 = int(input('Digite um número.\nNúmero 1: '))
n2 = int(input('Digite outro número.\nNúmero 2: '))


if n1 > n2:
    print(f'O primeiro número {n1=} é maior que o segundo número {n2=}')

elif n1 == n2:
    print(f'O valores de {n1=} e {n2=} são iguais')

else:
    print(f'O segundo número {n2=} é maior que o primeiro número {n1=}')



'''
    Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteiro, inform que não é um número inteiro.
'''
n1 = input('Ditite um número.\nNúmero: ')
n1_int = int(n1)

if not n1.isdigit():
    print('Isso não é um número inteiro.')
    

elif n1_int % 2 == 0:
    
    print(f'O número {n1_int} é PAR!')
    
else:
    print(f'O número {n1_int} é IMPAR!')



'''
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário discrito, exiba a saudação apropriada. Bom dia 0-11, Boa-tarce 12-17 e Boa-noite 18-23.
'''

hora = float(input('Qual a hora atual?\nHoras: '))

if hora >= 0 and hora <= 11:
    print('Bom-dia!')

elif hora >= 12 and hora <= 17:
    print('Boa-tarde!')

else:
    print('Boa-noite!')
'''
    Faça um programa que peça o primeiro nome do usuário, Se o nome tiver 4 letras ou menos escreva, "seu nome é curto"; se tiver entre 5 e 6 letras, escreva, "Seu nome é normal; maior que 6 escreva, "Seu nome é muito grande".
'''

nome = input('Digite seu nome.\nNome: ')
tamanho_nome = len(nome)
 
if tamanho_nome <= 4:
    print(f'Seu nome {nome} é curto.')

elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print(f'Seu nome {nome} é de um tamanho "normal".') 

else:
    print(f'Seu nome {nome} é muito longo.')





