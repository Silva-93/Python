# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True


    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return
        
        print(f'{self.nome} parou de filmar')
        self.filmando = False


    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar.')
            return
        
        print(f'{self.nome} está fotografando...')
        self.filmando = True       



c1 = Camera('Canon')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()