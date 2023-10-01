""" 
    Faça um programa que ler um salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$: 1250,00, calcule 10% de aumento. 
    Para salários igual ou inferiores a R1250,00, calcule 15% de aumento.
"""

salario = float(input('Digite o valor do seu salário para saber seu aumento.\nSalário: '))

aumento_10 = (salario * 10) / 100
aumento_15 = (salario * 15) / 100

novo_salario_15 = salario + aumento_15
novo_salario_10 = salario + aumento_10

if salario <= 1250:
    print(f'Você recebeu um aumento de 15%, com isso seu salário agora é de: {novo_salario_15}')
else:
    print(f'Você recebeu um aumento de 10%, com isso seu salário agora é de: {novo_salario_10}')