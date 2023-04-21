'''
    Maria pegou um empréstimo de 1.000.000 para realizar o pagamento em 5 anos.
    A data em que ela pegou o empréstimo foi 20/12/2020 eo vencimento de cada parcela é no dia 20 de cada mês.
    - Crie a data do empréstimo
    - Cria a data do final do empréstiom
    - Mostre todas as datas de vencimento e o valor de cada parcela
'''


from datetime import datetime
#  pip install python-dateutil
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1000000

data_emprestimo = datetime(2020, 12, 20)

tempo_emprestimo = relativedelta(years=5)

vencimento_emprestimo = data_emprestimo + tempo_emprestimo

data_parcela = data_emprestimo

data_parcelas = []

while data_parcela < vencimento_emprestimo:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)

valor_parcela = valor_emprestimo / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R${valor_emprestimo:,.2f} para pagar em {tempo_emprestimo.years} anos,'
    f'({numero_parcelas} meses), em parcelas de R$ {valor_parcela:,.2f}'
)