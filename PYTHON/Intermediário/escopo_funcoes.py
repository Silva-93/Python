'''
    Escopo significa o local onde aquele código pode atingir.
    Existe escopo global e local.
    O escopo global é o escope onde pode ser usado em todo o código.
    O escopo local só pode ser usado dentro da função onde é criado.
'''



# Função com escopo local
# A variável "x" dentro da função do pode ser usada na chamada da função, caso a mesma variável seja chamda fora do escopo da função, será mostrado um erro. Dizendo que a variável não foi definida.
def escopoLocal():
    x = 1
    print(x)

escopoLocal()
# print(x)

# Caso uma variável seja definida antes da criação da função, ela pode ser usada dentro da função.

x = 10

def escopoLocal2():
    print(x)

escopoLocal2()


# Para editar uma variável que está fora da função, é necessário declará-la como global

a = 100

def escopoLocal3():
    global a  # deixando a variável externa como global.
    ...
















