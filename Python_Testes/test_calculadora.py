import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    # Todos os métodos dessa classe devem começar com a palavra "test..."
    def test_soma_5_com_5_resultado_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_com_5_retorna_0(self):
        self.assertEqual(soma(-5, 5), 0)


    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (13, 10, 23),
            (23.5, 23.5, 47.0),
            (2, 5, 7),
            (10, 123, 133),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):  #  realizando subtestes
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)


    def test_soma_x_nao_e_int_ou_float_retouna_asserterror(self):
        with self.assertRaises(AssertionError):
            soma('11', 3)


    def test_soma_y_nao_e_int_ou_float_retouna_asserterror(self):
        with self.assertRaises(AssertionError):
            soma(11, '3')

unittest.main(verbosity=2)
