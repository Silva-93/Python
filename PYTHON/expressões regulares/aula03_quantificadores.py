import re

# Quantificadores
    # * -> 0 ou N vezes, é aplica ao caracter a esquerda do sinal
    # + -> 1 ou N vezes, é aplica ao caracter a esquerda do sinal
    # ? -> 0 ou 1 vez, pode ou não existir
    # {min, max} -> min ou max de vez | também pode ser uma quantidade "ilimitada" de vezes 

# Busca
    # . -> significa "qualquer caracter" por padrão ele não seleciona uma quebra de linha
    # [] -> significa um "conjunto" de caracteres
    # | -> significa "ou"

# ^ -> 
# $ -> 
# \ -> 
# () -> 


texto = '''
João trouxe       flores para sua amada namorada em 10 de janeiro de 1970, Maria era o nome dela.



Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainda faz aquile café com pão de queijo nas tardes de domingo. Também né! Sendo a bua mineira que é, nunca esquece seu famoso pão de queijo.
Não canso de ouvir a Maria: 
"Jooooooooooãoooooooo, o café té prontinho aqui. Veeemm!"
'''

print(re.findall(r'jo+ão+', texto, flags=re.I))

print(re.findall(r'jo*ão*', texto, flags=re.I))

print(re.findall(r'jo?ão*', texto, flags=re.I))

print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))  # o {1,} significa, repete 1 ou mais vezes

print(re.findall(r've{3}m{1,2}', texto, flags=re.I))  # {3} repete exatamente três vezes

print(re.sub(r'jo+ão+','Jose',  texto, flags=re.I))