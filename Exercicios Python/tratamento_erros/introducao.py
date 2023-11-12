try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a / b

except (ValueError, TypeError):
    print('Há um problema com o tipo do dado digitado.')

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por Zero.')

except KeyboardInterrupt:
    print('O usuário não informou os dados.')

except Exception as error:
    print(f'Foi encontrado o erro {error.__cause__}')

else:
    print(f'A divisão entre {a} e {b} é: {c:.2f}')

finally:
    print('Volte sempre!')