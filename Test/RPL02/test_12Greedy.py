from itertools import combinations
from unittest import TestCase

import Ejercicios.RPL02_Greedy.E12_kilometros_mafia as greedy


class TestGreedy12(TestCase):

	def _es_valida(self, seleccion):
		seleccion_ordenada = sorted(seleccion, key=lambda tramo: tramo[0])

		for i in range(1, len(seleccion_ordenada)):
			anterior = seleccion_ordenada[i - 1]
			actual = seleccion_ordenada[i]
			if actual[0] <= anterior[1]:
				return False

		return True

	def _optimo_por_fuerza_bruta(self, pedidos):
		mejor = 0

		for tamano in range(len(pedidos) + 1):
			for subconjunto in combinations(pedidos, tamano):
				if self._es_valida(subconjunto):
					mejor = max(mejor, len(subconjunto))

		return mejor

	def _assert_solucion_optima(self, pedidos):
		seleccion = greedy.asignar_mafias(pedidos)

		for pedido in seleccion:
			self.assertIn(pedido, pedidos)

		self.assertTrue(self._es_valida(seleccion))
		self.assertEqual(self._optimo_por_fuerza_bruta(pedidos), len(seleccion))

	def test_lista_vacia(self):
		self.assertEqual([], greedy.asignar_mafias([]))

	def test_un_solo_pedido(self):
		pedidos = [(1, 3.5)]
		self.assertEqual(pedidos, greedy.asignar_mafias(pedidos))

	def test_sin_solapamientos_elige_todos(self):
		pedidos = [(5, 6), (1, 2), (8, 9), (2.5, 3)]
		self.assertEqual(self._optimo_por_fuerza_bruta(pedidos), len(greedy.asignar_mafias(pedidos)))
		self.assertTrue(self._es_valida(greedy.asignar_mafias(pedidos)))

	def test_solapamiento_simple(self):
		pedidos = [(1, 4), (2, 3), (3.5, 5)]
		self._assert_solucion_optima(pedidos)

	def test_caso_clasico_de_intervalos(self):
		pedidos = [(1, 3.5), (3.3333, 8), (0, 1), (4, 5), (5.5, 7), (8, 9)]
		self._assert_solucion_optima(pedidos)

	def test_empates_en_la_cantidad_optima(self):
		pedidos = [(0, 4), (1, 2), (2.1, 3), (3.1, 4.1), (4.2, 5)]
		self._assert_solucion_optima(pedidos)

	def test_bordes_que_se_tocan_se_consideran_solapados(self):
		pedidos = [(1, 2), (2, 3), (3.01, 4)]
		seleccion = greedy.asignar_mafias(pedidos)

		self.assertTrue(self._es_valida(seleccion))
		self.assertEqual(2, len(seleccion))

	def test_intervalos_anidados_muchos_candidatos(self):
		pedidos = [(0, 10), (1, 2), (2.1, 3), (3.2, 4), (4.3, 5), (5.4, 6)]
		self._assert_solucion_optima(pedidos)
