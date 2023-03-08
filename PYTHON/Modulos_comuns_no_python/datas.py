"""
    Criando datas com módulo "datetime"
    
    datetime(ano, mês, dia)

    datetime(ano, mês, dia, horas, minutos, segundos)

    datetime.strptime('DATA', 'FORMATO')

    datetime.now()
"""

from datetime import datetime

hoje = datetime.now()
#print(hoje)  # datetime(ano, mês, dia, horas, minutos, segundos)

formato_data = '%d/%m/%Y'

data_atual = '08/03/2023'

data = datetime.strptime(data_atual, formato_data)
print(data)

print(data.srtftime(formato_data))