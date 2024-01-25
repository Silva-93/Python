import re
from pprint import pprint

# Grupos
    # () -> Define grupos, procura expecificamente o que está dentro dos () 

    # ()        \1 -> retrovisor
    # () ()     \1 \2
    # (()) ()   \1 \2 \3


texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4' , texto))



tags = re.findall(r'(<([pdiv]{1,3})>.+?<\/\2>)', texto) 

tags2 = re.findall(r'(<([pdiv]{1,3})>(.+?)<\/\2>)', texto)  # Selecionando o texto dentro das tags

tags3 = re.findall(r'<([pdiv]{1,3})>(?:.+?)<\/\1>', texto)   # ?: -> indica que o grupo será criado mas não será salvo


# [print(tag) for tag in tags]

# for tag in tags:
#     um, dois = tag
#     print(f'Grupo 1: {um} | Grupo 2: {dois}')

# print()

# for tag in tags2:
#     um, dois, tres = tag
#     print(tres)

# print()

# pprint(tags3)


cpf = '147.852.963-12'

# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))