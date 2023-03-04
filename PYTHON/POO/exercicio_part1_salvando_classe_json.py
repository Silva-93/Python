# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

FILE_PATH = r'C:\Users\Jouber\Desktop\file_json_class.json'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jhon', 33)
p2 = Person('Mary', 25)
p3 = Person('Lee', 18)

bd = [vars(p1), vars(p2), vars(p3)]

# Salvando o arquivo
def do_dump():
    with open(FILE_PATH, 'w') as file:
        json.dump(bd, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    do_dump()