from unittest import TestCase
from Grafo import grafo

import Ejercicios.RPL00_Grafos.EJ07_Grafo_diametro as ej


class TestRPL00GrafoDiametro(TestCase):
	def _crear_grafo(self, vertices, aristas):
		g = grafo.Grafo()
		for v in vertices:
			g.agregar_vertice(v)
		for v, w in aristas:
			g.agregar_arista(v, w)
		return g

	def test_grafo_vacio_diametro_cero(self):
		g = self._crear_grafo([], [])
		self.assertEqual(0, ej.diametro(g))

	def test_un_vertice_diametro_cero(self):
		g = self._crear_grafo(["A"], [])
		self.assertEqual(0, ej.diametro(g))

	def test_dos_vertices_unidos_diametro_uno(self):
		g = self._crear_grafo(["A", "B"], [("A", "B")])
		self.assertEqual(1, ej.diametro(g))

	def test_camino_de_seis_vertices_diametro_cinco(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E", "F"],
			[("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F")],
		)
		self.assertEqual(5, ej.diametro(g))

	def test_ciclo_de_cinco_vertices_diametro_dos(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "A")],
		)
		self.assertEqual(2, ej.diametro(g))

	def test_estrella_diametro_dos(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("A", "C"), ("A", "D"), ("A", "E")],
		)
		self.assertEqual(2, ej.diametro(g))

	def test_completo_de_cuatro_vertices_diametro_uno(self):
		vertices = ["A", "B", "C", "D"]
		aristas = []
		for i in range(len(vertices)):
			for j in range(i + 1, len(vertices)):
				aristas.append((vertices[i], vertices[j]))

		g = self._crear_grafo(vertices, aristas)
		self.assertEqual(1, ej.diametro(g))
