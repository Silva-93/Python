""" 
    Crie um programa que tenha uma a função leiaInt(), que vai funcionar de maneira semelhante a função input() só que fazendo a validação para aceitar apenas valores numéricos. 
"""

def leiaInt(numero):
    ok = False
    valor = 0
    while True:
        num = str(input(numero))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um valor inteiro válido.\033[m')

        if ok: 
            break
    
    return valor

num = leiaInt(f'Digite um número: ')
print(f'Você acaba de digitar o número: {num}')