""" 
    Context Manager com classes

    Você pode implementar seus próprios protocolos apenas implementando os dunder methods que o python vai usar. Isso é chamado de Duck Typing. Um conceito relacionado com tipagem dinâmica onde o python não está interessadono tipo, mas se alguns métodos existem no seu objeto para que ele funcione de forma adequada.
    
    Duck Typing:
    Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de pato.

    Para criar um context manager, os métodos __enter__ e __exit__ devem ser implementados. O método __exit__ receberá a classe de exceção, a exceção e traceback. Se ele retornar True, exceção no with será suprimidas.

    Ex de  contexto
        with open('path/file.txt', w) as file:
            ...
"""


class MyContextManager:
    def __init__(self, caminho, modo) -> None:
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None


    def __enter__(self):
        print('ABRINDO O ARQUIVO')
        self._arquivo = open(self.caminho, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, cls_exception, exception_, traceback_):
        print('FECHANDO O ARQUIVO')
        self._arquivo.close()

        
        


# criando um contexto | o retorno do __enter__ vai para "arquivo"
with MyContextManager('Aula31_context_manager.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
    print('CONTEXT', arquivo)

