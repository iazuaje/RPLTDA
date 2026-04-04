from unittest import TestCase
import Ejercicios.RPL01_DC.EJ03_raiz_cuadrada as dc

class TestDivisionYConquista(TestCase):

    def test_parte_entera_raiz_0(self):
        self.assertEqual(0, dc.parte_entera_raiz(0))

    def test_parte_entera_raiz_1(self):
        self.assertEqual(1, dc.parte_entera_raiz(1))

    def test_parte_entera_raiz_4(self):
        self.assertEqual(2, dc.parte_entera_raiz(4))

    def test_parte_entera_raiz_25(self):
        self.assertEqual(5, dc.parte_entera_raiz(25))

    def test_parte_entera_raiz_16(self):
        self.assertEqual(4, dc.parte_entera_raiz(16))

    def test_parte_entera_raiz_9(self):
        self.assertEqual(3, dc.parte_entera_raiz(9))

    def test_parte_entera_raiz_10(self):
        self.assertEqual(3, dc.parte_entera_raiz(10))

    def test_parte_entera_raiz_5(self):
        self.assertEqual(2, dc.parte_entera_raiz(5))