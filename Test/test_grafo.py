from unittest import TestCase
from Grafo import grafo
from Ejercicios.TP0.GrafoBipartito import bipartito

class TestGrafo(TestCase):
    _lista_vertices = ["a", "b", "c", "d", "e", "f"]

    def setUp(self):
        self.grafo = grafo.Grafo()
        for v in self._lista_vertices:
            self.grafo.agregar_vertice(v)

        self.grafo.agregar_arista("a", "f")
        self.grafo.agregar_arista("a", "c")
        self.grafo.agregar_arista("a", "d")
        self.grafo.agregar_arista("b", "f")
        self.grafo.agregar_arista("b", "e")

    def test_es_bipartito(self):
        self.assertTrue(bipartito.es_bipartito(self.grafo))
    
    def test_no_es_bipartito(self):
        self.grafo.agregar_arista("b", "a")
        self.assertFalse(bipartito.es_bipartito(self.grafo))

