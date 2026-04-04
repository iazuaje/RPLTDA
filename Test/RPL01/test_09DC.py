from unittest import TestCase
import Ejercicios.RPL01_DC.EJ09_mas_de_la_mitad as dc

class TestDivisionYConquista09(TestCase):
    
    def test_arregloPequeño(self):
        arr = [1]
        self.assertTrue(dc.mas_de_la_mitad(arr))
    
    def test_arregloCorrecto(self):
        arr = [1, 2, 3, 1, 1, 1]
        self.assertTrue(dc.mas_de_la_mitad(arr))
    
    def test_arregloIncorrecto(self):
        arr = [1, 1, 2, 3]
        self.assertFalse(dc.mas_de_la_mitad(arr))
    
    def test_otroArregloIncorrecto(self):
        arr = [1, 2, 1, 2, 3]
        self.assertFalse(dc.mas_de_la_mitad(arr))

    def test_dos_elementos_iguales(self):
        arr = [7, 7]
        self.assertTrue(dc.mas_de_la_mitad(arr))

    def test_dos_elementos_distintos(self):
        arr = [7, 8]
        self.assertFalse(dc.mas_de_la_mitad(arr))

    def test_mayoria_justa_en_par(self):
        arr = [2, 2, 2, 1]
        self.assertTrue(dc.mas_de_la_mitad(arr))

    def test_mitad_exacta_no_alcanza(self):
        arr = [3, 3, 4, 4]
        self.assertFalse(dc.mas_de_la_mitad(arr))

    def test_mayoria_no_contigua(self):
        arr = [5, 1, 5, 2, 5, 3, 5]
        self.assertTrue(dc.mas_de_la_mitad(arr))

    def test_negativos_con_mayoria(self):
        arr = [-1, -1, -1, 2, 3]
        self.assertTrue(dc.mas_de_la_mitad(arr))

    def test_negativos_sin_mayoria(self):
        arr = [-2, -2, -1, -1, 0]
        self.assertFalse(dc.mas_de_la_mitad(arr))

    def test_candidato_distribuido_en_mitades(self):
        arr = [9, 1, 9, 2, 9, 3, 9, 4, 9]
        self.assertTrue(dc.mas_de_la_mitad(arr))

    def test_sin_mayoria_en_impar(self):
        arr = [1, 2, 3, 1, 2]
        self.assertFalse(dc.mas_de_la_mitad(arr))
    
    def test_vacio(self):
        arr = []
        self.assertFalse(dc.mas_de_la_mitad(arr))