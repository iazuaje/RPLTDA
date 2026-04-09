from unittest import TestCase
from Grafo import grafo

import Ejercicios.RPL00_Grafos.EJ03_Grafo_es_arbol as ej


class TestRPL00GrafoEsArbol(TestCase):
	def _crear_grafo(self, vertices, aristas):
		g = grafo.Grafo()
		for v in vertices:
			g.agregar_vertice(v)
		for v, w in aristas:
			g.agregar_arista(v, w)
		return g

	def test_un_vertice_es_arbol(self):
		g = self._crear_grafo(["A"], [])
		self.assertTrue(ej.es_arbol(g))

	def test_camino_simple_es_arbol(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")],
		)
		self.assertTrue(ej.es_arbol(g))

	def test_estrella_es_arbol(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("A", "C"), ("A", "D"), ("A", "E")],
		)
		self.assertTrue(ej.es_arbol(g))

	def test_ciclo_no_es_arbol(self):
		g = self._crear_grafo(
			["A", "B", "C", "D"],
			[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
		)
		self.assertFalse(ej.es_arbol(g))

	def test_conexo_con_arista_extra_no_es_arbol(self):
		g = self._crear_grafo(
			["A", "B", "C", "D"],
			[("A", "B"), ("B", "C"), ("C", "D"), ("A", "C")],
		)
		self.assertFalse(ej.es_arbol(g))

	def test_conectado_aciclico_con_v_menos_1_aristas_es_arbol(self):
		g = self._crear_grafo(
			["A", "B", "C", "D"],
			[("A", "B"), ("C", "D"), ("A", "C")],
		)
		self.assertTrue(ej.es_arbol(g))

	def test_desconectado_sin_ciclos_no_es_arbol(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("B", "C"), ("D", "E")],
		)
		self.assertFalse(ej.es_arbol(g))

	def test_grafo_vacio_no_es_arbol(self):
		g = self._crear_grafo([], [])
		self.assertFalse(ej.es_arbol(g))
