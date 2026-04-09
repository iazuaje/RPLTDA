from unittest import TestCase
from Grafo import grafo

import Ejercicios.RPL00_Grafos.EJ01_Ciclo_en_grafo_no_dirigido as ej



class TestRPL00CicloEnGrafoNoDirigido(TestCase):
	def _crear_grafo(self, vertices, aristas):
		g = grafo.Grafo()
		for v in vertices:
			g.agregar_vertice(v)
		for v, w in aristas:
			g.agregar_arista(v, w)
		return g

	def _assert_ciclo_valido(self, g, ciclo):
		self.assertIsNotNone(ciclo)
		self.assertIsInstance(ciclo, list)

		# Permitimos [a, b, c, a] o [a, b, c].
		if len(ciclo) >= 2 and ciclo[0] == ciclo[-1]:
			ciclo = ciclo[:-1]

		self.assertGreaterEqual(len(ciclo), 3)
		self.assertEqual(len(ciclo), len(set(ciclo)))

		for i in range(len(ciclo)):
			v = ciclo[i]
			w = ciclo[(i + 1) % len(ciclo)]
			self.assertTrue(g.estan_unidos(v, w), f"La arista ({v}, {w}) no existe en el grafo")

	def test_triangulo_devuelve_ciclo(self):
		g = self._crear_grafo(
			["A", "B", "C"],
			[("A", "B"), ("B", "C"), ("C", "A")],
		)

		ciclo = ej.encontrar_ciclo(g)
		self._assert_ciclo_valido(g, ciclo)

	def test_arbol_no_tiene_ciclo(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")],
		)

		self.assertIsNone(ej.encontrar_ciclo(g))

	def test_desconectado_con_una_componente_ciclica(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E", "F"],
			[("A", "B"), ("B", "C"), ("C", "A"), ("D", "E")],
		)

		ciclo = ej.encontrar_ciclo(g)
		self._assert_ciclo_valido(g, ciclo)

	def test_ciclo_de_4_vertices(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("D", "E")],
		)

		ciclo = ej.encontrar_ciclo(g)
		self._assert_ciclo_valido(g, ciclo)

	def test_grafo_vacio(self):
		g = self._crear_grafo([], [])
		self.assertIsNone(ej.encontrar_ciclo(g))

	def test_un_solo_vertice(self):
		g = self._crear_grafo(["A"], [])
		self.assertIsNone(ej.encontrar_ciclo(g))
