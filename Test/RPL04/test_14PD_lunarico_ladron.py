from itertools import combinations
from unittest import TestCase

import Ejercicios.RPL04_PD.E14_lunatico_ladron as pd


class TestRPL04LunaticoLadron(TestCase):
	def _resolver_funcion_objetivo(self):
		if hasattr(pd, "lunatico"):
			return pd.lunatico
		if hasattr(pd, "lunatico_ladron"):
			return pd.lunatico_ladron
		self.fail("No se encontro la funcion objetivo. Defini lunatico(ganancias) o lunatico_ladron(ganancias)")

	def _resolver(self, ganancias):
		funcion = self._resolver_funcion_objetivo()
		return funcion(ganancias)

	def _es_valida(self, ganancias, seleccion):
		n = len(ganancias)
		if n == 0:
			return seleccion == []

		if any((not isinstance(i, int)) or i < 0 or i >= n for i in seleccion):
			return False

		if seleccion != sorted(seleccion):
			return False

		for i, j in combinations(seleccion, 2):
			if abs(i - j) == 1 or {i, j} == {0, n - 1}:
				return False

		return True

	def _ganancia(self, ganancias, seleccion):
		return sum(ganancias[i] for i in seleccion)

	def _optimo_fuerza_bruta(self, ganancias):
		n = len(ganancias)
		mejor = 0
		for tam in range(n + 1):
			for subconjunto in combinations(range(n), tam):
				if self._es_valida(ganancias, list(subconjunto)):
					mejor = max(mejor, self._ganancia(ganancias, subconjunto))
		return mejor

	def _assert_solucion_optima(self, ganancias):
		seleccion = self._resolver(ganancias)

		self.assertIsNotNone(seleccion)
		self.assertTrue(self._es_valida(ganancias, seleccion))
		self.assertEqual(self._optimo_fuerza_bruta(ganancias), self._ganancia(ganancias, seleccion))

	def test_lista_vacia(self):
		self.assertEqual([], self._resolver([]))

	def test_una_casa(self):
		ganancias = [7]
		sel = self._resolver(ganancias)
		self.assertEqual([0], sel)
		self.assertTrue(self._es_valida(ganancias, sel))

	def test_dos_casas_elige_la_mejor(self):
		ganancias = [3, 10]
		sel = self._resolver(ganancias)
		self.assertEqual([1], sel)
		self.assertTrue(self._es_valida(ganancias, sel))

	def test_tres_casas_elige_la_mayor_unica(self):
		ganancias = [2, 9, 4]
		sel = self._resolver(ganancias)
		self.assertEqual([1], sel)
		self.assertTrue(self._es_valida(ganancias, sel))

	def test_cuatro_casas_alternadas(self):
		ganancias = [5, 1, 5, 1]
		sel = self._resolver(ganancias)
		self.assertEqual([0, 2], sel)
		self.assertTrue(self._es_valida(ganancias, sel))

	def test_cuatro_casas_con_primera_y_ultima_altas(self):
		ganancias = [8, 1, 1, 8]
		sel = self._resolver(ganancias)
		self._assert_solucion_optima(ganancias)
		self.assertTrue(self._es_valida(ganancias, sel))

	def test_caso_clasico(self):
		ganancias = [6, 7, 1, 30, 8, 2, 4]
		self._assert_solucion_optima(ganancias)

	def test_repetidos_y_varias_soluciones_optimas(self):
		ganancias = [4, 4, 4, 4, 4]
		self._assert_solucion_optima(ganancias)

	def test_instancia_mediana(self):
		ganancias = [2, 10, 1, 1, 10, 2, 8, 3]
		self._assert_solucion_optima(ganancias)
