from collections import deque

def es_arbol(g):
    if len(g) == 0:
        return False

    cantidad_aristas = 0
    visitados = set()
    padres = {}
    cola = deque()

    vertice_inicial = g.vertice_aleatorio()
    padres[vertice_inicial] = None

    visitados.add(vertice_inicial)
    cola.append(vertice_inicial)

    while len(cola) != 0: 
        v = cola.popleft()
        for w in g.adyacentes(v):
            if w not in visitados:
                cantidad_aristas += 1
                visitados.add(w)
                padres[w] = v
                cola.append(w)
            elif w != padres[v]:
                #Hay un ciclo
                cantidad_aristas += 1

    return ((cantidad_aristas == (len(g.obtener_vertices()) - 1)) and len(visitados) == len(g.obtener_vertices()))