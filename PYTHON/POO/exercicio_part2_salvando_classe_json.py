import json
from exercicio_part1_salvando_classe_json import FILE_PATH, Person, do_dump



with open(FILE_PATH, 'r') as file:
    people = json.load(file)

    # Expandindo o arquivo com os dados json
    p1 = Person(**people[0])
    p2 = Person(**people[1])
    p3 = Person(**people[2])

    print(p1.name, p1.age)
    print(p2.name, p2.age)
    print(p3.name, p3.age)