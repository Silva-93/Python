from modulo_fatorial_dobro_triplo import fatorial, dobro, triplo

num = int(input('Digite um número para saber seu fatorial: '))
fat = fatorial(num)

print(f'O fatorial de {num} é: {fat}')
print(f'O dobro de {num} é: {dobro(num)}')
print(f'O triplo de {num} é: {triplo(num)}')