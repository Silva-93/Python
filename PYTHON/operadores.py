"""
    + -> Adição

    - -> Subtração

    * -> Multiplicação

    / -> Divisão 

    // -> Divisão inteira

    ** -> Potência

    Níveis de precedência dos operadores.

    1° ()
    
    2° **
    
    3° *  /  //  %
    
    4° +  =
"""

adicao = 10 + 10
print(f'Adição {adicao}')

subtracao = 10 - 5
print(f'Subtração {subtracao}')

multiplicacao = 10 * 10
print(f'Multiplicação {multiplicacao}')

divisao = 10 / 2
print(f'Divisão {divisao}')

divisao_inteira = 10 // 2.2
print(f'Divisão inteira {divisao_inteira}')

potencia = 10**2
print(f'Potência {potencia}')

resto_divisao = 55 % 2
print(f'Resto da divisão {resto_divisao}')


#  EXERCÍCIO

#  cálculo IMC

nome = input('Digite seu nome: ')

peso = float(input('Digite seu peso: '))

altura = float(input('Digite sua altura: '))

imc = peso / altura**2

print(f'{nome}, seu peso é {peso}kg e sua altura é {altura}m com isso seu IMC é: {imc:.2f}')


'''
    Operadores relacionais
   
    >   Maior que
    
    <   Menor que
    
    >=  Maior ou igual a
    
    <=  Menor ou igual a
    
    !=  Diferente de
    
    ==  Igual a
'''