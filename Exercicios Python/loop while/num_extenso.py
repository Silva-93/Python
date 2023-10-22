cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quantorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um valor entre 0 e 20.\nValor: '))

    if 0 <= num <= 20:
        break
    print('Digite um valor entre 0 e 20.')

print(f'Você digitou o número "{cont[num]}"')