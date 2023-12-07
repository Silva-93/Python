""" 
    As instâncias podem carregar estados
"""


class Camera:
    def __init__(self, marca, filme=False):
        self.marca = marca
        self.filme = filme


    def filmar(self):
        if self.filme:
            print(f'{self.marca} Já está filmando.')
            return  # será executado se o método já tiver sido chamado

        print(f'{self.marca} está filmando...')
        self.filme = True  # tornando o estado como verdadeiro.

camera1 = Camera('Canon')
camera2 = Camera('Sony')

camera1.filmar()
camera1.filmar()


















