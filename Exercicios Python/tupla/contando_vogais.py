""" 
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve motrar para cada palavra, quais são as suas vogais. 
"""

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro')


for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end=' ')
    for letras in palavra:
        if letras.lower() in 'aeiou':
            print(f'"{letras}"', end=' ')