def soma(x, y):

    #verifica se "x" é um número inteiro ou real
    assert isinstance(x, (int, float)), 'x deve ser um número inteiro ou real'  
    assert isinstance(y, (int, float)), 'y deve ser um número inteiro ou real'  
    return x + y
