from unittest import TestCase
from Grafo import grafo

import Ejercicios.RPL00_Grafos.EJ05_Grafo_obtener_orden as ej


class TestRPL00GrafoObtenerOrden(TestCase):
	def _crear_grafo_dirigido(self, vertices, aristas):
		g = grafo.Grafo(dirigido=True)
		for vertice in vertices:
			g.agregar_vertice(vertice)
		for origen, destino in aristas:
			g.agregar_arista(origen, destino)
		return g

	def _assert_orden_topologico_valido(self, vertices, aristas, orden):
		self.assertIsInstance(orden, list)
		self.assertEqual(len(vertices), len(orden))
		self.assertCountEqual(vertices, orden)

		posicion = {vertice: i for i, vertice in enumerate(orden)}
		for origen, destino in aristas:
			self.assertLess(
				posicion[origen],
				posicion[destino],
				f"La dependencia ({origen} -> {destino}) no se respeta en el orden devuelto",
			)

	def test_grafo_lineal(self):
		vertices = ["C1", "C2", "C3", "C4"]
		aristas = [("C1", "C2"), ("C2", "C3"), ("C3", "C4")]
		g = self._crear_grafo_dirigido(vertices, aristas)

		orden = ej.obtener_orden(g)
		self._assert_orden_topologico_valido(vertices, aristas, orden)

	def test_dag_con_ramas(self):
		vertices = ["C1", "C2", "C3", "C4", "C5", "C6"]
		aristas = [("C1", "C2"), ("C1", "C3"), ("C2", "C4"), ("C3", "C4"), ("C4", "C5")]
		g = self._crear_grafo_dirigido(vertices, aristas)

		orden = ej.obtener_orden(g)
		self._assert_orden_topologico_valido(vertices, aristas, orden)

	def test_dag_con_varias_componentes(self):
		vertices = ["A", "B", "C", "D", "E", "F"]
		aristas = [("A", "B"), ("C", "D"), ("D", "E")]
		g = self._crear_grafo_dirigido(vertices, aristas)

		orden = ej.obtener_orden(g)
		self._assert_orden_topologico_valido(vertices, aristas, orden)

	def test_grafo_sin_aristas(self):
		vertices = ["A", "B", "C", "D"]
		aristas = []
		g = self._crear_grafo_dirigido(vertices, aristas)

		orden = ej.obtener_orden(g)
		self._assert_orden_topologico_valido(vertices, aristas, orden)

	def test_grafo_vacio(self):
		g = self._crear_grafo_dirigido([], [])
		self.assertEqual([], ej.obtener_orden(g))

	def test_grafo_con_ciclo_devuelve_vacio(self):
		vertices = ["A", "B", "C"]
		aristas = [("A", "B"), ("B", "C"), ("C", "A")]
		g = self._crear_grafo_dirigido(vertices, aristas)

		self.assertEqual([], ej.obtener_orden(g))
