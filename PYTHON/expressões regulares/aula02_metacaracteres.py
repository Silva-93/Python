import re

# Busca
    # . -> significa "qualquer caracter" por padrão ele não seleciona uma quebra de linha
    # [] -> significa um "conjunto" de caracteres
    # | -> significa "ou"

# Quantificadores
    # * -> 0 ou N vezes, é aplica ao caracter a esquerda do sinal
    # + -> 1 ou N vezes, é aplica ao caracter a esquerda do sinal
    # ? -> 0 ou 1 vez, pode ou não existir
    # {min, max} -> min ou max de vez | também pode ser uma quantidade "ilimitada" de vezes 

# ^ -> 
# $ -> 
# \ -> 
# () -> 


texto = '''
João trouxe       flores para sua amada namorada em 10 de janeiro de 1970, Maria era o nome dela.



Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria, hoje sua esposa, ainda faz aquile café com pão de queijo nas tardes de domingo. Também né! Sendo a bua mineira que é, nunca esquece seu famoso pão de queijo.
Não canso de ouvir a Maria: 
"Jooooooooooãoooooooo, o café té prontinho aqui. Veeeemm!"
'''

print(re.findall(r'João|Maria', texto) )  # retorna uma lista com João e Maria

print(re.findall(r'ad....', texto))  # a ocorrência começa com "ad" o resto pode ser qualquer caracter. A quantidade de pontos indica aquandidade de caracteres após o início

print(re.findall(r'[Jj]oão|[Mm]aria', texto))

print(re.findall(r'[a-zA-Z]aria', texto))  # [a-z] -> qualquer letra de a até z

print(re.findall(r'jOãO|MaRia', texto, flags=re.I))  # "I" (IGNORECASE) não diferencia letas maiúscula de menúscula 






