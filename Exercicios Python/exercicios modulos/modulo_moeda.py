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




















