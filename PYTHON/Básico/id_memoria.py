'''
    flag -> marca um local
    
    None -> não tem valor
    
    is -> é alguma coisa (tipo, valor, identidadae)
    
    is not -> não é alguma coisa (tipo, valor, identidadae)
    
    id -> Identidade
'''

v1 = 'a'
v2 = 'a'
print(id(v1))  #  Mostra a identidade da variável na memória, o local que está
print(id(v2))
#  Como as duais variáveis têm o mesmo valor, ambas são localizadas no mesmo local da memória. O python busco o elemento pelo seu ID da memória.


condicao = False

if condicao:
    print('Faça algo')

else:
    print('Não faça algo')

























