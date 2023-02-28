# count é um iterador sem fim (itertools) -> Funciona de maneira parecida com o range
from itertools import count

c1 = count(8, 8)  # Indo de 8 a 100 pulando de 8 em 8

for i in c1:
    if i >= 100:
        break
    print(i)
