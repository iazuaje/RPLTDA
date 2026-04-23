from itertools import combinations
from unittest import TestCase

from Grafo import grafo
import Ejercicios.RPL03_BT.E14_dominating_set_min as ej


class TestRPL03DominatingSet(TestCase):
	def _resolver_funcion_objetivo(self):
		if hasattr(ej, "dominating_set_min"):
			return ej.dominating_set_min
		if hasattr(ej, "dominating_set"):
			return ej.dominating_set
		self.fail(
			"No se encontro la funcion objetivo. Defini dominating_set_min(grafo) o dominating_set(grafo)"
		)

	def _resolver(self, g):
		funcion = self._resolver_funcion_objetivo()
		return funcion(g)

	def _crear_grafo(self, vertices, aristas):
		g = grafo.Grafo()
		for v in vertices:
			g.agregar_vertice(v)
		for v, w in aristas:
			g.agregar_arista(v, w)
		return g

	def _es_dominating_set(self, g, candidatos):
		dset = set(candidatos)
		for v in g.obtener_vertices():
			if v in dset:
				continue

			dominado = False
			for w in g.adyacentes(v):
				if w in dset:
					dominado = True
					break

			if not dominado:
				return False
		return True

	def _assert_solucion_valida(self, g, solucion):
		self.assertIsNotNone(solucion)
		self.assertTrue(self._es_dominating_set(g, solucion))

		vertices_grafo = set(g.obtener_vertices())
		for v in solucion:
			self.assertIn(v, vertices_grafo)

	def _assert_solucion_minima(self, g, solucion):
		self._assert_solucion_valida(g, solucion)

		vertices = g.obtener_vertices()
		objetivo = len(set(solucion))

		for k in range(objetivo):
			for subset in combinations(vertices, k):
				if self._es_dominating_set(g, subset):
					self.fail("La solucion no es minima: existe un dominating set mas chico")

	def test_grafo_vacio_dominating_set_vacio(self):
		g = self._crear_grafo([], [])
		solucion = self._resolver(g)

		self._assert_solucion_minima(g, solucion)
		self.assertEqual(0, len(set(solucion)))

	def test_un_vertice_dominating_set_tamanio_uno(self):
		g = self._crear_grafo(["A"], [])
		solucion = self._resolver(g)

		self._assert_solucion_minima(g, solucion)
		self.assertEqual(1, len(set(solucion)))

	def test_una_arista_dominating_set_tamanio_uno(self):
		g = self._crear_grafo(["A", "B"], [("A", "B")])
		solucion = self._resolver(g)

		self._assert_solucion_minima(g, solucion)
		self.assertEqual(1, len(set(solucion)))

	def test_camino_de_cuatro_vertices_dominating_set_tamanio_dos(self):
		g = self._crear_grafo(
			["A", "B", "C", "D"],
			[("A", "B"), ("B", "C"), ("C", "D")],
		)
		solucion = self._resolver(g)

		self._assert_solucion_minima(g, solucion)
		self.assertEqual(2, len(set(solucion)))

	def test_ciclo_de_cinco_vertices_dominating_set_tamanio_dos(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "A")],
		)
		solucion = self._resolver(g)

		self._assert_solucion_minima(g, solucion)
		self.assertEqual(2, len(set(solucion)))

	def test_estrella_dominating_set_centro_unico(self):
		g = self._crear_grafo(
			["A", "B", "C", "D", "E"],
			[("A", "B"), ("A", "C"), ("A", "D"), ("A", "E")],
		)
		solucion = set(self._resolver(g))

		self._assert_solucion_minima(g, solucion)
		self.assertEqual({"A"}, solucion)

	def test_completo_de_cuatro_vertices_dominating_set_tamanio_uno(self):
		vertices = ["A", "B", "C", "D"]
		aristas = []
		for i in range(len(vertices)):
			for j in range(i + 1, len(vertices)):
				aristas.append((vertices[i], vertices[j]))

		g = self._crear_grafo(vertices, aristas)
		solucion = self._resolver(g)

		self._assert_solucion_minima(g, solucion)
		self.assertEqual(1, len(set(solucion)))

	def test_dos_componentes_estrella_dominating_set_tamanio_dos(self):
		g = self._crear_grafo(
			["A", "B", "C", "X", "Y", "Z"],
			[("A", "B"), ("A", "C"), ("X", "Y"), ("X", "Z")],
		)
		solucion = self._resolver(g)

		self._assert_solucion_minima(g, solucion)
		self.assertEqual(2, len(set(solucion)))
