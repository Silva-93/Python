import json

CAMINHO_ARQUIVO = 'Aula09-salvando-em-JSON.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Instâncias da classe
p1 = Pessoa('José', 33)
p2 = Pessoa('Maria', 21)
p3 = Pessoa('Renato', 18)

# Adicionando as instaâncias noma lista
bd = [vars(p1), vars(p2), vars(p3)]


# Criando o arquivo JSON com os dados da classe
def salvar_json():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('Salvando os dados em JSON')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    salvar_json()