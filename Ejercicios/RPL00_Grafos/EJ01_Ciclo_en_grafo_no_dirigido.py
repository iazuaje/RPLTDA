def encontrar_ciclo(g):
    '''
    Devuelve una lista de vertices que conforman el ciclo. En el segundo ejemplo, 
    debería devolver [A, B, C] (o [B, C, A], etc...). 
    Si no hay ciclo, debe devolver None. 
    '''

    visitados = set()
    padres = {}
    lista_vertices = g.obtener_vertices()

    for v in lista_vertices:
        if v not in visitados:
            padres[v] = None
            ciclo = dfs_ciclo(g, v, visitados, padres)
            if ciclo is not None:
                return ciclo
    return None

def dfs_ciclo(g, vertice, visitados, padres):
    visitados.add(vertice)

    for w in g.adyacentes(vertice):
        if w not in visitados:
            padres[w] = vertice
            ciclo = dfs_ciclo(g, w, visitados, padres)
            if ciclo is not None:
                return ciclo
        elif w != padres[vertice]:
            return reconstruir_ciclo(vertice, w, padres)
    return None

def reconstruir_ciclo(v, w, padres):
    camino_v = []
    actual = v
    while actual != w:
        camino_v.append(actual)
        actual = padres[actual]
    camino_v.append(w)
    return camino_v