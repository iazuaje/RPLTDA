from collections import deque

def bfs_distancias(grafo, origen):
    distancia = {}
    visitados = set()
    
    distancia[origen] = 0
    visitados.add(origen)
    cola = deque([origen])
    
    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                distancia[w] = distancia[v] + 1
                visitados.add(w)
                cola.append(w)
    
    return distancia


def diametro(grafo):
    vertices = list(grafo.obtener_vertices())
    n = len(vertices)
    
    if n <= 1:
        return 0
    
    diametro_max = 0
    
    for v in vertices:
        distancias = bfs_distancias(grafo, v)
        if distancias:
            max_dist = max(distancias.values())
            if max_dist > diametro_max:
                diametro_max = max_dist
    
    return diametro_max