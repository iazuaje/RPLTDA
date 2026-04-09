from unittest import TestCase
from Grafo import grafo

import Ejercicios.RPL00_Grafos.EJ04_Grafo_a_n_aristas as ej


class TestRPL00GrafoANAristas(TestCase):
	def _crear_grafo_dirigido(self, vertices, aristas):
		g = grafo.Grafo(dirigido=True)
		for vertice in vertices:
			g.agregar_vertice(vertice)
		for origen, destino in aristas:
			g.agregar_arista(origen, destino)
		return g

	def test_n_cero_devuelve_solo_origen(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C"],
			[("A", "B"), ("B", "C")],
		)
		resultado = ej.a_n_aristas(g, "A", 0)
		self.assertEqual(["A"], resultado)

	def test_vertices_a_un_salto(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D"],
			[("A", "B"), ("A", "C"), ("B", "D")],
		)
		resultado = ej.a_n_aristas(g, "A", 1)
		self.assertCountEqual(["B", "C"], resultado)

	def test_vertices_a_dos_saltos(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D", "E", "F"],
			[("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "F")],
		)
		resultado = ej.a_n_aristas(g, "A", 2)
		self.assertCountEqual(["D", "E"], resultado)

	def test_no_incluye_vertices_a_menor_distancia(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D"],
			[("A", "B"), ("B", "C"), ("C", "D")],
		)
		resultado = ej.a_n_aristas(g, "A", 2)
		self.assertEqual(["C"], resultado)

	def test_grafo_con_ciclo_no_duplica_vertices(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D"],
			[("A", "B"), ("B", "C"), ("C", "A"), ("B", "D")],
		)
		resultado = ej.a_n_aristas(g, "A", 2)
		self.assertCountEqual(["C", "D"], resultado)

	def test_n_mayor_que_diametro_alcanzable_devuelve_vacio(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D"],
			[("A", "B"), ("B", "C")],
		)
		resultado = ej.a_n_aristas(g, "A", 4)
		self.assertEqual([], resultado)

	def test_desde_origen_sin_salidas(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C"],
			[("A", "B")],
		)
		resultado = ej.a_n_aristas(g, "C", 1)
		self.assertEqual([], resultado)
