'''
    São usada para impor condições no código, esperando uma ação para serem executados.
    Leitura -> Se ... acontecer execute o código
               Se ... não acontecer execute o outro código

    if   /   elif   /  else
    se   se não se    se não
'''

entrar = input('Você quer "entrar" ou "sair" ? ')


if entrar == 'entrar':
    print('Entrou')

elif entrar == 'sair':
    print('Saiu.')

else:
    print('Digite "entrar" ou "sair".')



























