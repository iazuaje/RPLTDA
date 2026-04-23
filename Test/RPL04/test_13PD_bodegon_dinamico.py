from collections import Counter
from itertools import combinations
from unittest import TestCase

import Ejercicios.RPL04_PD.E13_bodegon_dinamico as pd


class TestRPL04BodegonDinamico(TestCase):
	def _resolver_funcion_objetivo(self):
		if hasattr(pd, "bodegon_dinamico"):
			return pd.bodegon_dinamico
		if hasattr(pd, "bodegon"):
			return pd.bodegon
		self.fail(
			"No se encontro la funcion objetivo. Defini bodegon_dinamico(P, W) o bodegon(P, W)"
		)

	def _resolver(self, grupos, capacidad):
		funcion = self._resolver_funcion_objetivo()
		return funcion(grupos, capacidad)

	def _es_subsecuencia(self, seleccion, grupos):
		i = 0
		for g in grupos:
			if i < len(seleccion) and seleccion[i] == g:
				i += 1
		return i == len(seleccion)

	def _ocupacion_optima_fuerza_bruta(self, grupos, capacidad):
		mejor = 0
		n = len(grupos)

		for tam in range(n + 1):
			for idxs in combinations(range(n), tam):
				suma = sum(grupos[i] for i in idxs)
				if suma <= capacidad:
					mejor = max(mejor, suma)

		return mejor

	def _assert_solucion_valida(self, grupos, capacidad, solucion):
		self.assertIsNotNone(solucion)
		self.assertTrue(self._es_subsecuencia(solucion, grupos))

		# No debe inventar grupos que no existen en P.
		self.assertLessEqual(Counter(solucion), Counter(grupos))

		total = sum(solucion)
		self.assertLessEqual(total, capacidad)

	def _assert_solucion_optima(self, grupos, capacidad):
		solucion = self._resolver(grupos, capacidad)
		self._assert_solucion_valida(grupos, capacidad, solucion)

		self.assertEqual(
			self._ocupacion_optima_fuerza_bruta(grupos, capacidad),
			sum(solucion),
		)

	def test_caso_base(self):
		grupos = [2, 4, 5, 3]
		capacidad = 9
		self._assert_solucion_optima(grupos, capacidad)

	def test_lista_vacia(self):
		self.assertEqual([], self._resolver([], 10))

	def test_capacidad_cero(self):
		self.assertEqual([], self._resolver([1, 2, 3], 0))

	def test_todos_superan_capacidad(self):
		grupos = [5, 6, 7]
		capacidad = 4
		self.assertEqual([], self._resolver(grupos, capacidad))

	def test_todos_entran(self):
		grupos = [1, 2, 3]
		capacidad = 6
		self.assertEqual(grupos, self._resolver(grupos, capacidad))

	def test_repetidos_mantiene_orden_original(self):
		grupos = [3, 3, 3, 2]
		capacidad = 8
		solucion = self._resolver(grupos, capacidad)

		self._assert_solucion_optima(grupos, capacidad)
		self.assertTrue(self._es_subsecuencia(solucion, grupos))

	def test_prefiere_ocupacion_maxima_no_cantidad_de_grupos(self):
		grupos = [4, 4, 3, 3, 2]
		capacidad = 8
		solucion = self._resolver(grupos, capacidad)

		self._assert_solucion_optima(grupos, capacidad)
		self.assertEqual(8, sum(solucion))

	def test_instancia_mediana(self):
		grupos = [2, 5, 4, 7, 1, 3, 8]
		capacidad = 12
		self._assert_solucion_optima(grupos, capacidad)
