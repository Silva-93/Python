import math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))  # convertendo o angulo para radianos
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} tem:')
print(f'O SENO de {seno:.2f}')
print(f'O COSSENO de {cosseno:.2f}')
print(f'A TANGENTE de {tangente:.2f}')