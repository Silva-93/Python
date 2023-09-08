# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'

response = requests.get(url)

raw_html = response.text  # html do site

parsed_html = BeautifulSoup(raw_html, 'html.parser')  # Transformando o html em objetos python

# if parsed_html is not None:
#     print(parsed_html.title.text)  # Pegando o texto do titulo do html

top_jos_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jos_heading is not None:
    article = top_jos_heading.parent  # pegando o elemento acima do h2 
    
    if article is not None:   
        for p in article.select('p'):  # selecionando todas as tags p
            print(p.text)

