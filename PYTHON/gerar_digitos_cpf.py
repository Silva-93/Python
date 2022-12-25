"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
    *  *  *  *  *  *  *  *  *
*  7   4  6  8  2  4  8  9  0
    =  =  =  =  =  =  =  =  =
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

# GERANDO O PRIMEIRO DIGITO DO CPF

cpf_enviado = input('Digite seu CPF.\nCPF: ').replace('.', '').replace('-', '')

noveDigitos = cpf_enviado[:9]

contadorRegressivo1 = 10

resultadoDigito1 = 0

# iterando pelos digitos do cpf
for digito in noveDigitos:
    # somando e multiplicando os valores
    resultadoDigito1 += int(digito)*contadorRegressivo1
    
    contadorRegressivo1 -= 1

# multiplicando por 10 e buscando o resto da divisão e obtendo o primeiro digito
primeiroDigito = (resultadoDigito1 * 10) % 11

primeiroDigito = 0 if primeiroDigito > 9 else primeiroDigito
# print(primeiroDigito)





"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO, multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
   *   *  *  *  *  *  *  *  *  *
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   =   =  =  =  =  =  =  =  =  = 
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363

Multiplicar o resultado anterior por 10
363 * 10 = 3630

Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""


dezDigitos = cpf_enviado[:9]


contadorRegressivo2 = 11

resultadoDigito2 = 0

dezDigitos = noveDigitos + str(primeiroDigito)

# iterando pelos digitos do cpf
for digito in dezDigitos:
    # somando e multiplicando os valores
    resultadoDigito2 += int(digito)*contadorRegressivo2
    
    contadorRegressivo2 -= 1

# multiplicando por 10 e buscando o resto da divisão e obtendo o segundo digito
segundoDigito = (resultadoDigito2*10) % 11
segundoDigito = 0 if segundoDigito > 9 else segundoDigito

# print(segundoDigito)

# print(f'Os 2 últimos números do seu CPF é "{primeiroDigito}" e "{segundoDigito}"')


# VALIDANDO UM CPF

cpf_validado = f'{noveDigitos}{primeiroDigito}{segundoDigito}'

if cpf_enviado == cpf_validado:
    print(f'O CPF: {cpf_enviado} é válido.')

else:
    print('CPF inválido.')





















