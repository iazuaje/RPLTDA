from collections import deque
from Grafo import grafo

def es_bipartito(grafo : grafo.Grafo):
    colores = {}
    for vertice in grafo:
        if colores.get(vertice) is not None:
            continue

        colores[vertice] = 0
        colaVertices = deque([vertice])

        while len(colaVertices) > 0:
            verticeActual = colaVertices.popleft()
            for adyacente in grafo.adyacentes(verticeActual):
                if colores.get(adyacente) is None:
                    colores[adyacente] = 1 - colores[verticeActual]
                    colaVertices.append(adyacente)
                elif colores[adyacente] == colores[verticeActual]:
                    return False
    return True

