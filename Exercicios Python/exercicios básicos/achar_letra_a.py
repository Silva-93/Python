""" 
    Escreva um programa que leia uma frasa e mostre
        Quantas vezes a letra "a" apareceu
        Em que posição ela aparece pela primeira vez
        Em que posição ela aparece pela última vez
"""

frase = str(input('Digite uma frase: ')).upper()

print(f'A frase tem um total de {frase.count("A")} letras A')
print(f'A primeira letra "a" aparece na posição {frase.find("A")}')
print(f'A última vez que a letra "a" apareceu foi na posição {frase.rfind("A")}')  # Procura da direita para a esquerda