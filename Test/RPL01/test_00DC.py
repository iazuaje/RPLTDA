from unittest import TestCase
import Ejercicios.RPL01_DC.EJ00_arr_suma_maxima as dc


class TestMaxSubarrayDyC(TestCase):

    def test_todos_positivos(self):
        """Caso donde todos son positivos - debe devolver todo el array"""
        arr = [5, 3, 2, 4, -1]
        resultado = dc.max_subarray(arr)
        self.assertEqual([5, 3, 2, 4], resultado)

    def test_negativo_en_medio(self):
        """Caso con negativo en el medio del array"""
        arr = [5, 3, -5, 4, -1]
        resultado = dc.max_subarray(arr)
        self.assertEqual([5, 3], resultado)

    def test_dos_negativos(self):
        """Caso con dos negativos"""
        arr = [5, -4, 2, 4, -1]
        resultado = dc.max_subarray(arr)
        self.assertEqual([5, -4, 2, 4], resultado)

    def test_negativo_al_final(self):
        """Caso con negativo al final"""
        arr = [5, -4, 2, 4]
        resultado = dc.max_subarray(arr)
        self.assertEqual([5, -4, 2, 4], resultado)

    def test_negativos_al_comienzo(self):
        """Caso con negativos al comienzo"""
        arr = [-3, 4, -1, 2, 1, -5]
        resultado = dc.max_subarray(arr)
        self.assertEqual([4, -1, 2, 1], resultado)

    def test_array_vacio(self):
        """Caso array vacío"""
        arr = []
        resultado = dc.max_subarray(arr)
        self.assertEqual([], resultado)

    def test_un_elemento_positivo(self):
        """Caso un solo elemento positivo"""
        arr = [5]
        resultado = dc.max_subarray(arr)
        self.assertEqual([5], resultado)

    def test_un_elemento_negativo(self):
        """Caso un solo elemento negativo"""
        arr = [-3]
        resultado = dc.max_subarray(arr)
        self.assertEqual([-3], resultado)

    def test_dos_elementos(self):
        """Caso dos elementos"""
        arr = [1, 2]
        resultado = dc.max_subarray(arr)
        self.assertEqual([1, 2], resultado)

    def test_dos_elementos_negativos(self):
        """Caso dos elementos negativos"""
        arr = [-5, -3]
        resultado = dc.max_subarray(arr)
        self.assertEqual([-3], resultado)

    def test_suma_maxima_en_medio(self):
        """Caso donde la suma máxima está en el medio"""
        arr = [1, 2, -10, 5, 6, 7]
        resultado = dc.max_subarray(arr)
        self.assertEqual([5, 6, 7], resultado)

    def test_suma_maxima_al_final(self):
        """Caso donde la suma máxima está al final"""
        arr = [-2, -1, 3, 4, 5]
        resultado = dc.max_subarray(arr)
        self.assertEqual([3, 4, 5], resultado)

    def test_suma_maxima_al_comienzo(self):
        """Caso donde la suma máxima está al comienzo"""
        arr = [5, 4, 3, -10, -1]
        resultado = dc.max_subarray(arr)
        self.assertEqual([5, 4, 3], resultado)

    def test_todos_negativos(self):
        """Caso donde todos son negativos"""
        arr = [-5, -2, -8, -1]
        resultado = dc.max_subarray(arr)
        self.assertEqual([-1], resultado)

    def test_unico_positivo(self):
        """Caso con un solo positivo y resto negativos"""
        arr = [-5, 10, -2, -3]
        resultado = dc.max_subarray(arr)
        self.assertEqual([10], resultado)