""" 
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sanbendo que a cada lintro de tinta, pinta uma área de 2m².
"""

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'Com uma parede {largura}m de largura e {altura}m de altura, sua área é de {area}m². Com isso será necessário gastar {tinta}l de tinta.')