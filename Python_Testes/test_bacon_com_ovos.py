""" 
    TDD -> Test Driver Development (Desenvolvimento dirigido a testes)

    Red
    1° Criar o teste e ver falhar

    Green
    2° Criar o código e ver o teste passar

    Refactor
    3° Melhorar o código
"""
import unittest
from bacon_com_ovos import bacon_com_ovos

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_levanta_erro_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')
    

    def test_retorna_bacon_com_ovos_se_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)  # Multiplos de 3 e 5
        saida = 'Bacon com Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual = (bacon_com_ovos(entrada), saida)


    def test_retorna_passar_fome_se_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)  
        saida = 'Passar fome!'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual = (bacon_com_ovos(entrada), saida)


    def test_retorna_bacon_se_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12)  # Multiplos de 3 
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual = (bacon_com_ovos(entrada), saida)


    def test_retorna_ovos_se_for_multiplo_de_3(self):
        entradas = (5, 10, 20, 25)  # Multiplos de 5 
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual = (bacon_com_ovos(entrada), saida)




unittest.main(verbosity=2)
