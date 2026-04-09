from collections import deque

def es_conexo(grafo):

    if len(grafo) == 0:
        return True

    visitados = set()
    cola = deque()

    vertice_inicial = grafo.vertice_aleatorio()

    visitados.add(vertice_inicial)
    cola.append(vertice_inicial)

    while len(cola) != 0:
        v = cola.popleft()

        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                cola.append(w)

    return len(visitados) == len(grafo.obtener_vertices())