""" 
    Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
"""

metros = float(input('Quantos metros?\nMetros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
cm = metros * 100
mm = metros * 1000

print(f'A medida de {metros} metros são:')
print(f'{km}km Quilômetros')
print(f'{hm}hm Hectômetos')
print(f'{dam}dam Decâmetros')
print(f'{cm}cm Centímetros')
print(f'{mm}mm Milímetos')
