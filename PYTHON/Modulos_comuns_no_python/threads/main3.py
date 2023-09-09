from threading import Thread, Lock
from time import sleep

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()  # sempre que o códig entrar nesse método ele será "trancado" e não permite que "todo mundo" acesse o método
    
    def comprar(self, quantidade):
        self.lock.acquire()  # Liberando o método

        if self.estoque < quantidade:
            print('Não temos ingressos no estoque')
            self.lock.release()
            return
        
        sleep(1)
    
        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque} em estoque')

        self.lock.release()  # Liberando o método

if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 15):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
               
    print(ingressos.estoque)