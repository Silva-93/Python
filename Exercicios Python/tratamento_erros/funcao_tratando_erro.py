""" 
    Cria uma função chamada leiaInt(), incluindo a possibilidade da digitação de um número do tipo inválido. E crie uma função chamada leiaFloat() com as memas caracteristicas.
"""

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
        
        except KeyboardInterrupt:
            print('O usuário não digitou nenhum valor.')
            return 0
        
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))

        except (ValueError, TypeError):
            print('ERRO! Digite um número real válido.')

        except KeyboardInterrupt:
            print('O usuário não digitou nenhum valor.')
            return 0
        
        else:
            return num


numInt = leiaInt('Digite um valor inteiro: ')
numFloat = leiaFloat('Digite um valor real: ')

print(f'O valor inteiro digitado foi: {numInt}')
print(f'O valor real digitado foi: {numFloat}')