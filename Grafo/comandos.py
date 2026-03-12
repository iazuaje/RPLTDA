from Grafo.biblioteca import *

# ============================ COMANDOS ====================================

# ================================= CAMINO MAS CORTO ===========================
def camino_mas_corto(usuario_cancion, canciones, parametros):
    origen, destino = parametros.split(" >>>> ")

    if (origen not in canciones or destino not in canciones):
        return print('Tanto el origen como el destino deben ser canciones')

    _, padres = bfs_camino(usuario_cancion, origen, destino)
    if destino not in padres:
        return print('No se encontro recorrido')
    camino = armar_camino(padres, origen, destino)

    for i in range(len(camino) - 1):
        _, playlist = usuario_cancion.peso_arista(camino[i], camino[i + 1])
        if i % 2 == 0:
            print(f"{camino[i]} --> aparece en playlist --> ", end='')
            print(f"{playlist} --> de --> ", end='')
        else:
            print(f"{camino[i]} --> tiene una playlist --> ", end='')
            print(f"{playlist} --> donde aparece --> ", end='')

    print(f"{camino[len(camino) - 1]}")
    return


# ================================ MAS IMPORTANTES ===============================

def mas_importantes(mas_importantes, n):
    for i in range(n - 1):
        print(f"{mas_importantes[i]['nombre']}; ", end="")
    print(f"{mas_importantes[n - 1]['nombre']}")


# ==================================== RECOMENDACION ===============================

def recomendacion(usuario_cancion, canciones, parametros, usuarios):
    tipo, n, lista_canciones = parametros.split(maxsplit=2)
    lista_canciones = lista_canciones.split(" >>>> ")
    recomendaciones = {}
    lista_recomendaciones = []

    for vertice in usuario_cancion:
        recomendaciones[vertice] = 0
        if vertice in lista_canciones:
            recomendaciones[vertice] = 1

    for cancion in lista_canciones:
        camino = random_walk(usuario_cancion, cancion)
        pagerank_personalizado(usuario_cancion, recomendaciones, camino)

    for reco in recomendaciones:
        if reco not in lista_canciones:
            if reco in canciones and tipo == "canciones":
                lista_recomendaciones.append({
                    'nombre': reco,
                    'importancia': recomendaciones[reco]
                })
            elif reco in usuarios and tipo == "usuarios":
                lista_recomendaciones.append({
                    'nombre': reco,
                    'importancia': recomendaciones[reco]
                })
    lista_recomendaciones.sort(key=lambda x: x['importancia'], reverse=True)

    for i in range(int(n) - 1):
        print(f"{lista_recomendaciones[i]['nombre']}; ", end='')
    print(f"{lista_recomendaciones[int(n) - 1]['nombre']}")
    return


# ============================================ CICLO ===============================

def ciclo_canciones(canciones, parametros):
    n, origen = parametros.split(maxsplit=1)
    if int(n) < 3:
        print("No se encontro recorrido")
        return
    ciclo = ciclo_n(canciones, int(n), origen)
    if ciclo == None:
        print("No se encontro recorrido")
        return
    for i in range(len(ciclo) - 1):
        print(f"{ciclo[i]} --> ", end='')
    print(f"{ciclo[len(ciclo) - 1]}")
    return


# ================================= RANGO =========================================
def rango_canciones(entre_canciones, parametros):
    n, cancion = parametros.split(maxsplit=1)
    en_rango = bfs_en_rango(entre_canciones, cancion, limite=int(n))
    print(en_rango)
    return
