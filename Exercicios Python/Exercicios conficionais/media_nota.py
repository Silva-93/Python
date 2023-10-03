""" 
    Faça um programa que leia duas notas e calcule a média delas e mostre se o aluno está aprovado, de recuperação ou reprovado.
"""

nota1 = float(input('Digite sua 1° nota: '))
nota2 = float(input('Digite sua 2° nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua média foi: {media} \033[31mREPROVADO!!!\033[0;0m')

elif media >= 5 and media < 6.9:
    print(f'Sua média foi: {media} \033[33mRECUPERAÇÃO\033[0;0m')

else:
    print(f'Sua média foi: {media} \033[32mAPROVADO\033[0;0m')