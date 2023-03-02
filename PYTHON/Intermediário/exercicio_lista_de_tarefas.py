# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json

def listar(tarefas):
    print()
    if not tarefas:
        print('Não há itens para ser listados.')
        return
    
    print('Tarefas')
    for tarefa in tarefas:
        print(f'\t{tarefa}')




def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Não há itens para ser desfeito.')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)




def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Não há itens para serem refeitos.')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)



def adcionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Nada foi digitado.')
        return
    
    tarefas.append(tarefa)



# Funções para salvar em arquivos json

def ler(tarefas, caminho_arquivo):
    dados = []

    try:
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
    
    except FileNotFoundError:
        print('Arquivo não exite')
        salvar(tarefas, caminho_arquivo)

    return dados



def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w') as arquivo:
        dados = json.dump(
            tarefas,
            arquivo,
            indent=2,
            ensure_ascii=False)
        
        return dados

CAMINHO_ARQUIVO = r'C:\Users\Jouber\Desktop\arquivo.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: [1]listar, [2]desfazer, [3]refazer, [4]adicionar')
    tarefa = input('Digite uma tarefa ou comando.\n-> ')

    if tarefa == '1':
        listar(tarefas)
        continue
    
    elif tarefa == '2':
        desfazer(tarefas, tarefas_refazer)
        continue

    elif tarefa == '3':
        refazer(tarefas, tarefas_refazer)
        continue
        
    else:
        adcionar(tarefa, tarefas)
        continue

salvar(tarefas, CAMINHO_ARQUIVO)