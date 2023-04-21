"""
    Criando datas com módulo "datetime"
    
    datetime(ano, mês, dia)

    datetime(ano, mês, dia, horas, minutos, segundos)

    datetime.strptime('DATA', 'FORMATO')

    datetime.now()
"""

from datetime import datetime

data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')

hoje = datetime.now()
print(hoje)

""" 
print(data.strftime('%d/%m/%Y'))  # Mostra a data
print(data.strftime('%d/%m/%Y %H:%M'))  # Mostra a data, hora e minutos
print(data.strftime('%d/%m/%Y %H:%M:%S'))  # Mostra a data, hora, minutos e segundos
print(data.strftime('%Y'), data.year)  # Mostra o ano
print(data.strftime('%d'), data.day)  # Mostra o dia
print(data.strftime('%m'), data.month)  # Mostra o mês
print(data.strftime('%H'), data.hour)  # Mostra a hora
print(data.strftime('%M'), data.minute)  # Mostra os minutos
print(data.strftime('%S'), data.second)  # Mostra os segundos
"""