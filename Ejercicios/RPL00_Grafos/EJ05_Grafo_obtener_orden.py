from collections import deque

def obtener_orden(grafo):
    'Devolver una lista con un posible orden válido'

    vertices = grafo.obtener_vertices()

    grados = {}
    orden = []
    cola = deque()

    for v in vertices:
        grados[v] = 0

    for v in vertices:
        for w in grafo.adyacentes(v):
            grados[w] = grados[w] + 1

    for v in vertices:
        if grados[v] == 0:
            cola.append(v)

    while len(cola) != 0:
        v = cola.popleft()
        orden.append(v)

        for w in grafo.adyacentes(v):
            grados[w] = grados[w] - 1
            if grados[w] == 0:
                cola.append(w)

    if len(orden) != len(vertices):
        return []

    return orden