""" 
    Faça um programa que leia o salário de um funcionário e adicione 15% de aumento
"""

salario_atual = float(input('Digite seu salário\nR$: '))
aumento_15 = (salario_atual + 15) / 100
novo_salario = salario_atual + aumento_15

print(f'Salário atual: {salario_atual}')
print(f'Aumento de 15%: {aumento_15}')
print(f'Novo salário: {novo_salario:.2f}')