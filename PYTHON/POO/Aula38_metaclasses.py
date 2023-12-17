""" 
    Metaclasses são o tipo das classes, estão acima dos objects

    Em python, tudo é um objeto (classes também são objetos), então qual é o tipo de uma classe? (type) 
    Seu objeto é uma instância da sua classe, sua classe é uma instância de type (type é uma classe) 
        type('Name', (Bases,), __dict__)

    Ao criar uma classe, coisas ocorrem por padrão nesse ordem:
        __new__ da metaclass é chamado e cria a nova classe
        __call__ da metaclass é chamdo com os argumentos e chama;
            __new__ da class com os argumentos (cria a instância)
            __init__ da class com os argumentos
        __call__ da metaclass termina a execução

    Métodos importantes da metaclass
        __new__(mcs, name, bases, dct) (cria a classe)
        __call__(cls, *args, **kwargs) (cria e inicializa a instância)

    "Metaclasses são magias mais progundas do que 99% dos usuários dveriam se preocupar. Se você quer saber se precisa delas, não precisa (as pessoas que realmente precisam delas sabem com certeza que precisam delas e não precisam de uma explicação sobre o porquê)" - Tim Peters (CPython Core Developer)
"""






















