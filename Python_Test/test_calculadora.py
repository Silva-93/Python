import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma_5_com_5_resultado_10(self):
        self.assertEqual(soma(5, 5), 10)


unittest.main(verbosity=2)