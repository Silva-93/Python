""" 
    Desenvolva um programa que leia duais notas de um aluno e mostra a média dele.
"""

nota1 = float(input('Digite sua 1° nota: '))
nota2 = float(input('Digite sua 2° nota: '))
media = (nota1 + nota2) / 2

print(f'1° nota: {nota1}\n2° nota:{nota2}\nmédia: {media:.2f}')