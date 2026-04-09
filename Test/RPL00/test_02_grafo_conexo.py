from unittest import TestCase
from Grafo import grafo

import Ejercicios.RPL00_Grafos.EJ02_Grafo_es_conexo as ej


class TestRPL00GrafoConexo(TestCase):
    def _crear_grafo(self, vertices, aristas):
        g = grafo.Grafo()
        for v in vertices:
            g.agregar_vertice(v)
        for v, w in aristas:
            g.agregar_arista(v, w)
        return g

    def test_un_vertice_es_conexo(self):
        g = self._crear_grafo(["A"], [])
        self.assertTrue(ej.es_conexo(g))

    def test_dos_vertices_unidos_es_conexo(self):
        g = self._crear_grafo(["A", "B"], [("A", "B")])
        self.assertTrue(ej.es_conexo(g))

    def test_dos_vertices_sin_union_no_es_conexo(self):
        g = self._crear_grafo(["A", "B"], [])
        self.assertFalse(ej.es_conexo(g))

    def test_grafo_lineal_es_conexo(self):
        g = self._crear_grafo(
            ["A", "B", "C", "D", "E"],
            [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")],
        )
        self.assertTrue(ej.es_conexo(g))

    def test_dos_componentes_no_es_conexo(self):
        g = self._crear_grafo(
            ["A", "B", "C", "D", "E"],
            [("A", "B"), ("B", "C"), ("D", "E")],
        )
        self.assertFalse(ej.es_conexo(g))

    def test_con_un_aislado_no_es_conexo(self):
        g = self._crear_grafo(
            ["A", "B", "C", "D"],
            [("A", "B"), ("B", "C")],
        )
        self.assertFalse(ej.es_conexo(g))

    def test_ciclo_conexo(self):
        g = self._crear_grafo(
            ["A", "B", "C", "D"],
            [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
        )
        self.assertTrue(ej.es_conexo(g))
		
    def test_ciclo_vacio(self):
        g = self._crear_grafo([],[])
        self.assertTrue(ej.es_conexo(g))
		
