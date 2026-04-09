from collections import deque

def a_n_aristas(grafo, v, n):
    'Devolver una lista con los vértices que cumplen la propiedad'

    visitados = set()
    distancias = {}
    cola = deque()

    cola.append(v)
    distancias[v] = 0
    visitados.add(v)
    
    while len(cola) != 0:
        v = cola.popleft()

        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                distancias[w] = distancias[v] + 1
                cola.append(w)

    resultado = []

    for key in distancias.keys():
        if (distancias[key] == n):
            resultado.append(key)

    return resultado