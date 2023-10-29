""" 
    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1° Nota: '))
    nota2 = float(input('2° Nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar? [S/N]: ')).upper()
    if opcao == 'N':
        break

print('-=' * 30)
print(f'{"N°":<4}{"NOME":<10}{"NOTA":>8}')
print('-=' * 30)

for index, aluno in enumerate(ficha):
    print(f'{index:<4} {aluno[0]:<10} {aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar a nota de qual aluno: (999 para finalizar). '))
    if opc == 999:
        break
    
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')