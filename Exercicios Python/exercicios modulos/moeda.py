""" 
    Crie um programa chamado modulo_moeda.py que tenhas as funções aumentar(), diminuir(), dobro() e metade(). Faça outro programa que importe modulo_moeda.py e use suas funções. 
"""

import modulo_moeda

num = float(input('Digite um valor.\nR$: '))

metade = modulo_moeda.metade(num, True)
dobro = modulo_moeda.dobro(num, True)
porcetagem = modulo_moeda.porcentagem(num, 10, True)
aumento = modulo_moeda.aumento(num, 10, True)
desconto = modulo_moeda.diminuir(num, 10, True)

print(f'A metade de {modulo_moeda.moeda(num)} é: {metade}')
print(f'O dobro de {modulo_moeda.moeda(num)} é: {dobro}')
print(f'10% de {modulo_moeda.moeda(num)} é: {porcetagem}')
print(f'O valor com o aumento de 10% ficou: {aumento}')
print(f'O valor com 10% de desconto ficou: {desconto}')