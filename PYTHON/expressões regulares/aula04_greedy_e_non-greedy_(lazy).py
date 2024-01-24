import re

# Quantificadores
    # greedy (guloso)  
    # non-greedy(lazy) (não guloso)

    # * -> 0 ou N vezes, é aplica ao caracter a esquerda do sinal
    # + -> 1 ou N vezes, é aplica ao caracter a esquerda do sinal
    # ? -> 0 ou 1 vez, pode ou não existir
    # {min, max} -> min ou max de vez | também pode ser uma quantidade "ilimitada" de vezes  


texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))  # greedy

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))  # non-greedy

























