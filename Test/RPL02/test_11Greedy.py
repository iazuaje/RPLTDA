from unittest import TestCase
from collections import Counter
import Ejercicios.RPL02_Greedy.E11_bolsas_supermercado as gd

class TestGreedy11(TestCase):

    def _assert_solucion_valida(self, capacidad, productos, bolsas):
        # No se pierden ni duplican productos
        usados = [p for bolsa in bolsas for p in bolsa]
        self.assertEqual(Counter(productos), Counter(usados))

        # Ninguna bolsa supera la capacidad
        for bolsa in bolsas:
            self.assertLessEqual(sum(bolsa), capacidad)

    def test_caso_base(self):
        productos = [4, 2, 1, 3, 5]
        bolsas = gd.bolsas(5, productos)

        self._assert_solucion_valida(5, productos, bolsas)
        self.assertEqual(3, len(bolsas))

        # Comparación sin depender del orden de bolsas
        canon = sorted([tuple(sorted(b)) for b in bolsas])
        esperado = sorted([tuple(sorted([5])), tuple(sorted([4, 1])), tuple(sorted([3, 2]))])
        self.assertEqual(esperado, canon)

    def test_lista_vacia(self):
        bolsas = gd.bolsas(5, [])
        self.assertEqual([], bolsas)

    def test_todos_entran_en_una_bolsa(self):
        productos = [2, 2, 1]
        bolsas = gd.bolsas(5, productos)

        self._assert_solucion_valida(5, productos, bolsas)
        self.assertEqual(1, len(bolsas))

    def test_best_fit_mejora_caso_tipico(self):
        # Caso donde Best Fit Decreasing logra 4 bolsas
        productos = [6, 6, 5, 5, 5, 5, 4, 4]
        bolsas = gd.bolsas(10, productos)

        self._assert_solucion_valida(10, productos, bolsas)
        self.assertEqual(4, len(bolsas))

    def test_repetidos_y_capacidad_exacta(self):
        productos = [3, 3, 2, 2, 2, 1, 1, 1]
        bolsas = gd.bolsas(4, productos)

        self._assert_solucion_valida(4, productos, bolsas)