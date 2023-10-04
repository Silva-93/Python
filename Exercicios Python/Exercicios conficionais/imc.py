""" 
    Faça um programa que leia a altura e o  peso de uma pesso e calcule seu índece de massa corporal (IMC)
"""

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura**2

if imc < 18.5:
    print(f'Seu IMC é: {imc:.2f}. Você está abaixo do peso.')

elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é: {imc:.2f}. Você está no peso ideal.')

elif imc >= 25 and imc < 30:
    print(f'Seu IMC é: {imc:.2f}. Você está acima do peso.')

elif imc >=30  and imc < 40:
    print(f'Seu IMC é: {imc:.2f}. Você está obeso.')

elif imc > 40:
    print(f'Seu IMC é: {imc:.2f}. Você está com obesidade mórbida.')