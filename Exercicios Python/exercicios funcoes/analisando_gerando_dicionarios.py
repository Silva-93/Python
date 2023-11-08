


def notas(*n, sit=False):

    nota = {}
    nota['total'] = len(n)
    nota['maior'] = max(n)
    nota['menor'] = min(n)
    nota['media'] = round(sum(n) / len(n), 2)

    if sit: 
        if nota['media'] >= 7:
            nota['situacao'] = 'Aprovado'

        elif nota['media'] >= 5:
            nota['situacao'] = 'Razoável'

        else:
            nota['situacao'] = 'Ruim'
    
    return nota

resp = notas(7.5, 3.2, 5.5, sit=True)

print(resp)










