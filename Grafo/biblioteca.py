from random import choice
from collections import deque
from Grafo import grafo

def grados_salida(grafo):
    grados = {}
    for v in grafo:
        grados[v] = len(grafo.adyacentes(v))
    return grados


def vertices_entrada(grafo):
    vertices = {}
    for v in grafo:
        vertices[v] = []
    for v in grafo:
        for w in grafo.adyacentes(v):
            vertices[w].append(v)
    return vertices


# ===================================== RECORRIDO ===============================


def bfs_camino(grafo, origen, destino=None):
    visitados = set()
    distancia = {}
    padre = {}

    distancia[origen] = 0
    padre[origen] = None
    visitados.add(origen)

    q = deque()
    q.append(origen)

    while q:
        v = q.popleft()
        if v == destino:
            return distancia, padre
        for w in grafo.adyacentes(v):
            if w not in visitados:
                distancia[w] = distancia[v] + 1
                padre[w] = v
                q.append(w)
                visitados.add(w)

    return distancia, padre


def bfs_en_rango(grafo, origen, limite=1):
    en_rango = 0
    visitados = set()
    distancia = {}

    distancia[origen] = 0
    visitados.add(origen)

    q = deque()
    q.append(origen)

    while q:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                distancia[w] = distancia[v] + 1
                if distancia[w] == limite:
                    en_rango += 1
                if distancia[w] > limite:
                    return en_rango
                q.append(w)
                visitados.add(w)

    return en_rango


def armar_camino(padre, origen, destino):
    camino = []
    if destino not in padre:
        return None
    while destino != origen:
        camino.append(destino)
        destino = padre[destino]
    camino.append(destino)
    return camino[::-1]


def existe_camino(camino):
    return len(camino) > 2


# ======================================= PAGERANK ===============================


def suma_pagerank(grafo, v, PR, L, E, d=0.85):
    resultado = 0
    for w in E[v]:
        resultado += PR[w] / L[w]
    return d * resultado


def pagerank(grafo, d=0.85, iterador=100):
    PR = {}
    N = len(grafo)
    L = grados_salida(grafo)
    E = vertices_entrada(grafo)

    factor_aleatorio = (1 - d) / N

    # Inicializamos los valores del grafo
    for v in grafo:
        PR[v] = factor_aleatorio

    # Calculamos los pagerank de cada vertice
    for _ in range(iterador):
        for v in grafo:
            PR[v] = factor_aleatorio + suma_pagerank(grafo, v, PR, L, E)

    return PR


def random_walk(grafo, origen, largo=100):
    camino = []
    camino.append(origen)
    v = origen
    for _ in range(largo):
        v = choice(grafo.adyacentes(v))
        camino.append(v)
    return camino


def pagerank_personalizado(
        grafo, recomendaciones, camino, largo=20, iteracion=100
):
    for _ in range(iteracion):
        i = 1
        while i <= largo:
            v = camino[i - 1]
            w = camino[i]
            recomendaciones[w] += recomendaciones[v] / len(
                grafo.adyacentes(v)
            )
            i += 1


# =============================================================================

# ====================================FUNCIONES DE CICLOS=======================

def validar_final(grafo, actual, origen, ciclo, n):
    return len(ciclo) == n and origen in grafo.adyacentes(actual)


def _ciclo_n(grafo, visitados, ciclo, actual, origen, n):
    ciclo.append(actual)
    visitados.add(actual)

    if validar_final(grafo, actual, origen, ciclo, n):
        return True

    if len(ciclo) < n:
        for w in grafo.adyacentes(actual):
            if w not in visitados:
                if _ciclo_n(grafo, visitados, ciclo, w, origen, n):
                    return True

    visitados.remove(actual)
    ciclo.pop()

    return False


def ciclo_n(grafo, n, origen):
    visitados = set()
    ciclo = []
    if _ciclo_n(grafo, visitados, ciclo, origen, origen, n):
        ciclo.append(origen)
        return ciclo
    return None

def _dfs_bipartito(grafo: grafo.Grafo, origen, visitados, distancias, v1, v2):
    for w in grafo.adyacentes(origen):
        if w not in visitados:
            visitados.add(w)
            if distancias[origen] % 2 == 0:
                v2.add(w)
            else: v1.add(w)
            distancias[w] = distancias[origen] + 1
            _dfs_bipartito(grafo, w, visitados, distancias, v1, v2)

def _es_bipartito(grafo, origen, visitados):
    v1 = set()
    v2 = set()
    distancias = {}
    distancias[origen] = 0
    v1.add(origen)
    _dfs_bipartito(grafo, origen, visitados, distancias, v1, v2)

    es_bipartito_flag = True

    for v in v1:
        for w in grafo.adyacentes(v):
            if w in v1: es_bipartito_flag = False

    for v in v2:
        for w in grafo.adyacentes(v):
            if w in v2: es_bipartito_flag = False

    return es_bipartito_flag

def es_bipartito(grafo : grafo.Grafo):
    cantidad_vertices = len(grafo)
    visitados = set()
    es_bipartito_flag = True
    while (len(visitados) < cantidad_vertices):
        for v in grafo:
            if v not in visitados:
                visitados.add(v)
                es_bipartito_flag = _es_bipartito(grafo, v, visitados)
    return es_bipartito_flag