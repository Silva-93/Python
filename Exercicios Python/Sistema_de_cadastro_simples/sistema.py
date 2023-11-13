from interface import *
from time import sleep


while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoa', 'Listar Pessoas', 'Sair do Sistema'])

    if resposta == 1:
        cabecalho('Opção 1')
    
    elif resposta == 2:
        cabecalho('Opção 2')
    
    elif resposta == 3: 
        cabecalho('\033[36mSaindo do sistema.\033[m')
        break
    
    else:
        cabecalho('\033[31mOpção inválida\033[m')

    sleep(2)