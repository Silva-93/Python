'''
    isinstance -> É usado para verificar se o objeto é de um determinado tipo

    Exemplos: isinstance(variavel, str) -> verifica se a variável é do tipo str, o mesmo segue para todos os tipos de dados
'''

lista = ['a', 1, 1.1, True, [0,1,2,3], (1,2), {0, 1}, {'nome': 'Fulano'}]


for itens in lista:
    if isinstance(itens, set):  # só exibe o item que é do tipo set
        print(f'"{itens}" ')
    
    if isinstance(itens, str):
        print(f'"{itens}" ')  # só exibe o item que é do tipo str

    if isinstance(itens, (int, float)):  # só exibe o item que é do tipo int ou do tipo float
        print(f'"{itens}" ')
