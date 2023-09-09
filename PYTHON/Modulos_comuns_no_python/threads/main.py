
""" 
    Executando mais de 1 serviços ao mesmo tempo
"""

from threading import Thread
from time import sleep

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()  # Inicializando o init da Tread

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Thread 1', 4)
t1.start()  # iniciando a thread

t2 = MeuThread('Thread 2', 2)
t2.start()  # iniciando a thread

t3 = MeuThread('Thread 3', 6)
t3.start()  # iniciando a thread

for i in range(20):  # Threat principal
    print(i)
    sleep(1)

#  Todas as Treads vão ser executadas independente do for, quando chegar o tempo de execução das mesmas elas serão executadas junto ao for