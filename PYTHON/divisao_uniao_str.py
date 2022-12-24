'''
    split -> Divide uma string

    join -> Une uma string

'''





frase = 'Olha só, como isso é interessante.'

lista_palavras = frase.split()  #  Quando o .split é usado sem parâmetro, ele irá quebrar a string a cada "espaço" formando uma lista com cada palavra separada.
print(lista_palavras)

lista_palavras2 = frase.split(',')  # A string será quebrada quando acher uma "vírgula", formado uma lista com 2 valores
print(lista_palavras2)



frases_unidas = '-'.join('abc')  # para cada letra da string terá um "-" unindo as letras.
print(frases_unidas)






















