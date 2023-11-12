""" 
    Escreva um programa que sorteie um aluno dentre quatro para apagar o quadro.
"""

from random import choice, shuffle


aluno1 = str(input('1° aluno: '))
aluno2 = str(input('2° aluno: '))
aluno3 = str(input('3° aluno: '))
aluno4 = str(input('4° aluno: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista_alunos)  # Uma escolha dentro da lista
print(f'O aluno escolhido foi: {escolhido}') 


""" 
    Escreva um programa que leia uma lista de alunos e embaralhe a mesma para a apresentação
"""

print('=============================')

estudante1 = str(input('1° aluno: '))
estudante2 = str(input('2° aluno: '))
estudante3 = str(input('3° aluno: '))
estudante4 = str(input('4° aluno: '))

lista_estudantes = [estudante1, estudante2, estudante3, estudante4]

shuffle(lista_estudantes)  # embaralhando a lista

print(f'A ordem de apresentação escolhida foi: {lista_estudantes}')
