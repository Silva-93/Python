from interface import *
from arquivo import *
from time import sleep


arq = 'sistema_de_cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        lerArquivo(arq)
    
    elif resposta == 2:
        cabecalho('NOVO CADASTRO.')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    
    elif resposta == 3: 
        cabecalho('\033[36mSaindo do sistema.\033[m')
        break
    
    else:
        cabecalho('\033[31mOpção inválida\033[m')

    sleep(1)