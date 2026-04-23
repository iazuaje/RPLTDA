def obtener_lista_aristas(grafo):
    aristas = []
    vistas = set()

    for nodo in grafo:
        for adyacente in grafo.adyacentes(nodo):
            if (adyacente, nodo) not in vistas:
                vistas.add((nodo, adyacente))
                aristas.append((nodo, adyacente))

    return aristas

def quitar_aristas_incidentes(nodo, aristas):
    nueva_lista = []
    for v, w in aristas:
        if nodo != v and nodo != w:
            nueva_lista.append((v, w))
    return nueva_lista

def backtracking(aristas_pendientes, solucion_actual, mejor_solucion):
    if len(solucion_actual) >= len(mejor_solucion):
        return mejor_solucion
    
    if len(aristas_pendientes) == 0 :
        return solucion_actual.copy()

    v, w = aristas_pendientes[0]
    mejor = mejor_solucion

    if v in solucion_actual:
        aristas_v = quitar_aristas_incidentes(v, aristas_pendientes)
        mejor = backtracking(aristas_v, solucion_actual, mejor)
    else:
        solucion_actual.append(v)
        aristas_v = quitar_aristas_incidentes(v, aristas_pendientes)
        mejor = backtracking(aristas_v, solucion_actual, mejor)
        solucion_actual.pop()

    if w in solucion_actual:
        aristas_w = quitar_aristas_incidentes(w, aristas_pendientes)
        mejor = backtracking(aristas_w, solucion_actual, mejor)
    else:
        solucion_actual.append(w)
        aristas_w = quitar_aristas_incidentes(w, aristas_pendientes)
        mejor = backtracking(aristas_w, solucion_actual, mejor)
        solucion_actual.pop()
    
    return mejor

def vertex_cover_min(grafo):
    aristas = obtener_lista_aristas(grafo)
    mejor_solucion = grafo.obtener_vertices()

    return backtracking(aristas, [], mejor_solucion)