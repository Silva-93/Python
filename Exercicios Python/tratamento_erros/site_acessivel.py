""" 
    Crie um programa que teste se um determinado site está acessível pelo computador do usuário
"""

import urllib.request

try:
    site = urllib.request.urlopen('https://mangaschan.net/')

except urllib.error.URLerror:
    print('O site "mangaschan" não está acessível')

else:
    print('Site "mangaschan" acessado com sucesso.')
    # print(site.read())  #  -> Mostra o HTML da página do site















