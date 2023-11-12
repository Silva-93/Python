""" 
    Faça u mprograma que tenha uma função chamda area(), que receba as dimenções de um terreno retangular(largura e altura) e mostre a área do terreno.
"""

def msg(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(msg)
    print('-' * tam)

msg('    Calculando a área do terreno.')

def area(largura, altura):
    area = largura * altura
    return f'A área de {largura} x {altura} é: {area:.2f}.'

largura = float(input('Largura: '))
altura = float(input('Altura: '))

print(area(largura, altura))

