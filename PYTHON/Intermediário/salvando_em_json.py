import json

""" pessoa = {
    'nome': 'Jouber',
    'sobrenome': 'Vicente',
    'enderecos': [
        {'rua': 'R1', 'numero': 4},
        {'rua': 'R2', 'numero': 5},
    ],
    'altura': 1.75,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': False,
    'nada': None,
}

# Salvando as configurações num arquivo.

with open('arquivo.json', 'w') as arquivo:
    json.dump(
        pessoa, 
        arquivo,
        ensure_ascii=False,
        indent=2
    ) """


# Lendo o arquivo json
with open('arquivo.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
