from unittest import TestCase
from Grafo import grafo

import Ejercicios.RPL00_Grafos.EJ06_Grafo_componentes_debiles as ej


class TestRPL00GrafoComponentesDebiles(TestCase):
	def _crear_grafo_dirigido(self, vertices, aristas):
		g = grafo.Grafo(dirigido=True)
		for vertice in vertices:
			g.agregar_vertice(vertice)
		for origen, destino in aristas:
			g.agregar_arista(origen, destino)
		return g

	def test_grafo_vacio_tiene_cero_componentes(self):
		g = self._crear_grafo_dirigido([], [])
		self.assertEqual(0, ej.cantidad_componentes_debiles(g))

	def test_un_vertice_tiene_una_componente(self):
		g = self._crear_grafo_dirigido(["A"], [])
		self.assertEqual(1, ej.cantidad_componentes_debiles(g))

	def test_cadena_dirigida_es_una_componente_debil(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D"],
			[("A", "B"), ("B", "C"), ("C", "D")],
		)
		self.assertEqual(1, ej.cantidad_componentes_debiles(g))

	def test_direccion_opuesta_tambien_conecta_debilmente(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D"],
			[("B", "A"), ("C", "B"), ("D", "C")],
		)
		self.assertEqual(1, ej.cantidad_componentes_debiles(g))

	def test_dos_componentes_separadas(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("B", "C"), ("D", "E")],
		)
		self.assertEqual(2, ej.cantidad_componentes_debiles(g))

	def test_componentes_con_vertices_aislados(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D", "E"],
			[("A", "B")],
		)
		self.assertEqual(4, ej.cantidad_componentes_debiles(g))

	def test_ciclo_y_otra_componente(self):
		g = self._crear_grafo_dirigido(
			["A", "B", "C", "D", "E", "F"],
			[("A", "B"), ("B", "C"), ("C", "A"), ("D", "E")],
		)
		self.assertEqual(3, ej.cantidad_componentes_debiles(g))
