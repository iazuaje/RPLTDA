def backtracking(i, vertices, cobertura, dominados, solucion_actual, mejor_solucion, total_vertices):
    if len(solucion_actual) >= len(mejor_solucion):
        return mejor_solucion

    if len(dominados) == total_vertices:
        return solucion_actual.copy()

    if i == total_vertices:
        return mejor_solucion

    v = vertices[i]
    mejor = mejor_solucion

    solucion_actual.append(v)
    dominados_incluyendo_v = dominados | cobertura[v]
    mejor = backtracking(i + 1,vertices, cobertura, dominados_incluyendo_v, solucion_actual, mejor, total_vertices)
    solucion_actual.pop()

    mejor = backtracking(i + 1, vertices, cobertura, dominados, solucion_actual, mejor, total_vertices)

    return mejor


def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    n = len(vertices)

    mejor_solucion = vertices.copy()
    cobertura = {}
    for vertice in vertices:
        cobertura[vertice] = set(grafo.adyacentes(vertice)) | {vertice}

    return backtracking(0, vertices, cobertura, set(), [], mejor_solucion, n)