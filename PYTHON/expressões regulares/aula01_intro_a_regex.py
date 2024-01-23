import re

# regex diferenciam letras maiúsculas de menúsculas
# findall -> Retorna todas as ocorrências do padrão que se quer encontrar dentro do texto. Retorna uma lista com todas as ocorrências
# search -> Encontra a primeira ocorrência e mostra qual índice ela está, retorna um objeto match. Retorna "None" caso a ocorrência não seja encontrada
# sub -> substitui algo dentro do texto
# compile -> compila expressões regulares

string = 'Este é um teste de expressões regulares. Isso está servindo de teste para aprender regex testando e testando várias vezes.'

print(re.search(r'teste', string))  # procurando a palavra "teste"

print(re.findall(r'teste', string))  

print(re.sub(r'teste', 'TESTANDO', string, count=1))  # o "count=1" faz com que apenas a primeira ocorrência seja substituida, se for "count=0", todas as ocorrências serão substituidas (padrão)  

print()

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('COMPILE', string))

















