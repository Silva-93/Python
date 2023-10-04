""" 
    Crie um programa que analisa as retas e digam se elas podem se tornar um triângulo e qual tipo de triângulo elas formam. 
"""

reta1 = float(input('Digite uma reta: '))
reta2 = float(input('Digite uma reta: '))
reta3 = float(input('Digite uma reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas podem formar um triângulo.')

    if reta1 == reta2 == reta3:
        print('As retas formam um triângulo EQUILÁTERO.')
    
    elif reta1 != reta2 != reta3 != reta1:
        print('As retas formam um triângulo ESCALENO.')

    else:
        print('As retas formam um triângulo ISÓSCELES.')

else:
    print('As retas não formam um triângulo.')