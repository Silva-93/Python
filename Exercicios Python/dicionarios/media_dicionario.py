



aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    aluno['situalção'] = 'Aprovado'

elif 5 <= aluno['media'] < 7:
    aluno['situalção'] = 'Recuperação'

else:
    aluno['situalção'] = 'Reprovado'

print('-=' * 30)

for keys, values in aluno.items():
    print(f'   - {keys} é igual a {values}')