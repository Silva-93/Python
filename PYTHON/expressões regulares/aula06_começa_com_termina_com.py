import re

# ^ -> Começa com ...
# $ -> Termina com ...
# [^a-z] -> Negação, qualquer coisa que não esteja um range entre [a-z]

cpf = '147.852.963-12'

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^a-z]+', cpf))  # negando tudo que esteja num range de [a-z]
print(re.findall(r'[^0-9]+', cpf))  # negando tudo que esteja num range de [0-9]