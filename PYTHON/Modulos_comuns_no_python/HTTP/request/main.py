""" 
    requets -> Para requisições HTTP

    pip install requests types-requests
"""
import requests

url = 'http://localhost:3333/'

response = requests.get(url)

print(response.status_code)  # Código de estatus da requisição
# print(response.headers)  # Cabeçalho da requisição
# print(response.content)  # Conteúdo do site em bytes
print(response.text)