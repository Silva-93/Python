""" 
    Programa que lê o que foi digitado e mostre seu tipo primitivo
"""

entrada = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(entrada)}')
print(f'Só tem espaços? {entrada.isspace()}')
print(f'É um número? {entrada.isnumeric()}')
print(f'É alfabético {entrada.isalpha()}')
print(f'É alfanumérico {entrada.isalnum()}')
print(f'Está em letras maiúsculas {entrada.isupper()}')
print(f'Está em letras minúsculas {entrada.islower()}')
print(f'Está em capitalizada?(com a 1° letra maiúscula) {entrada.istitle()}')
