'''
    AND -> Todas as condições devem ser verdadeiras

    OR -> Apenas um valor deve ser cnosiderado verdadeiro para a condição ser validada como verdadeira.

    NOT -> negação, inverte o valor de uma conedição

    IN -> dentro de ou entre algo

    IN NOT -> não dentro ou não entre algo

'''


entrada = input('[E]ntrar ou [S]air?').upper()

senha_digitada = input('Digite a senha.')

senha = '123456'

if entrada == 'E' and senha == senha_digitada:
    print('Entrar')

else:
    print('Sair')





entrada = input('[E]ntrar ou [S]air?')

senha_digitada = input('Digite a senha.')

senha = '123456'

if (entrada == 'E' or entrada == 'e') and senha == senha_digitada:
    print('Entrar')

else:
    print('Sair')




nome = 'Jouber'

#  Verificando se as letras estão dentro da palavra da variável

print('ber' in nome)
print('jou' in nome)
print('oub' in nome)
print('vic' in nome)





















