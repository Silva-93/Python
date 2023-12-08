from Aula09_salvando_a_classe_em_JSON_A import CAMINHO_ARQUIVO, Pessoa
import json


# lendo os dados do json
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    
    # recriando as instâncias da classe
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

