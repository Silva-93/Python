'''
    Closute e funções que retornam outras funções
'''

def criarSaudacao(saudacao):
    def saudar(nome):  # Cria uma função que não é executada no mesmo momento, mas salva na memória a executção da função principal "criarSaudacao"
        return f'{saudacao}, {nome}!'
    return saudar  #  Retorna a função, mas não executa a função


falar_bom_dia = criarSaudacao('Bom dia')
falar_boa_noite = criarSaudacao('Boa noite')

print(falar_bom_dia('Jouber'))  #  fechando a execução da função
print(falar_boa_noite('Jouber'))


for nome in ['Maria', 'Jose', 'Ana']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))


















