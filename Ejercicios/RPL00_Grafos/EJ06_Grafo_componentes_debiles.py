from collections import deque

def cantidad_componentes_debiles(grafo):
    vertices = grafo.obtener_vertices()
    visitados = set()
    componentes = 0

    vecinos = {}
    for v in vertices:
        vecinos[v] = set()

    for v in vertices:
        for w in grafo.adyacentes(v):
            vecinos[v].add(w)
            vecinos[w].add(v)
    
    for v in vertices:
        if v not in visitados:
            componentes += 1
            bfs_no_dirigido(v, vecinos, visitados)

    return componentes

def bfs_no_dirigido(origen, vecinos, visitados):
    cola = deque()
    cola.append(origen)
    visitados.add(origen)

    while len(cola) != 0:
        v = cola.popleft()
        for w in vecinos[v]:
            if w not in visitados:
                visitados.add(w)
                cola.append(w)