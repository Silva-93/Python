from threading import Thread
from time import sleep

# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar, args=('Olá mundo!', 5))
# t1.start()

# t2 = Thread(target=vai_demorar, args=('Olá mundo!', 3))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('Olá mundo!', 7))
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(.5)

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo!', 5))
t1.start()
# t1.join()  # juntando a threa a threa principal

while t1.is_alive():  # enquanto a thread estiver a tiva
    print('Esperando a thread.')
    sleep(2)

    