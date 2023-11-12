""" 
    Faça um programa que leia o comprimento de três retas e digo ao usuário e elas formam um triângulo ou não. 
"""

reta1 = float(input('Digite uma reta: '))
reta2 = float(input('Digite uma reta: '))
reta3 = float(input('Digite uma reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas formam um triângulo.')

else:
    print('As retas não formam um triângulo.')