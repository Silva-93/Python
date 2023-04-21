import calendar

"""
    Por padrão dia da semana começa com 0 até 6
    0 - Segunda
    1 - Terça
    2 - Quarta
    3 - Quinta
    4 - Sexta
    5 - Sabado
    6 - Domingo
"""

#print(calendar.calendar(2022))  # Mostra o calendário do ano especificado.

#                    year  month
#print(calendar.month(2020, 12))  # Mostra o calendário de um mês de um ano especificados.

print(calendar.monthrange(2021, 11))  # Mostra o último dia do mês