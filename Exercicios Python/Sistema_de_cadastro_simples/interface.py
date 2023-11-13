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


def linha(msg = 42):
    return '-' * msg


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())
    

def menu(lst):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lst:
        print(f'\033[33m{contador}\033[m - \033[32m{item}\033[m')
        contador += 1
    print(linha())
    opc = leiaInt('Escolha uma opção: ')
    return opc