""" 
    Crie um programa chamado modulo_moeda.py que tenhas as funções aumentar(), diminuir(), dobro() e metade(). Faça outro programa que importe modulo_moeda.py e use suas funções. 
"""
def porcentagem(numero=0, porcent=0, formato=False):
    perct = (numero * porcent) / 100
    return perct if formato is False else moeda(perct)


def aumento(preco=0, taxa=0, formato=False):
    porcent = preco + (preco * taxa) / 100
    return porcent if formato is False else moeda(porcent)


def diminuir(preco=0, taxa=0, formato=False):
    porcentagem = preco - (preco * taxa) / 100
    return porcentagem if formato is False else moeda(porcentagem)


def metade(numero=0, formato=False):
    metad = numero / 2
    return metad if formato is False else moeda(metad)


def dobro(numero=0, formato=False):
    dobr0 = numero * 2
    return dobr0 if formato is False else moeda(dobr0)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(numero, taxa=0, desconto=0):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35 ))
    print('-' * 35)

    print(f'Preço analisado: \t{moeda(numero)}')
    print(f'O dobro do preço é: \t{dobro(numero, True)}')
    print(f'A metado do preço é: \t{metade(numero, True)}')
    print(f'{taxa}% de aumento é: \t{aumento(numero, taxa, True)}')
    print(f'{desconto}% de desconto é: \t{diminuir(numero, desconto, True)}')
    print('-' * 35)




















