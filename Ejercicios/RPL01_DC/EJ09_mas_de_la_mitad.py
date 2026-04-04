def mas_de_la_mitad(arr):
    cantidad_elementos = len(arr)

    if (cantidad_elementos) == 0:
        return False

    if (cantidad_elementos) == 1:
        return True
    
    candidato = _mas_de_la_mitad(arr, 0, cantidad_elementos - 1)

    return verificar_candidato(candidato, arr, 0, cantidad_elementos - 1)

def _mas_de_la_mitad(arr, ini, fin):
    if ini >= fin:
        return arr[fin]

    mitad = (ini + fin) // 2

    candidato_izquierdo = _mas_de_la_mitad(arr, ini, mitad)
    candidato_derecho = _mas_de_la_mitad(arr, mitad + 1, fin)

    if candidato_izquierdo == candidato_derecho:
        return candidato_derecho
    
    if (verificar_candidato(candidato_izquierdo, arr, ini, fin)):
        return candidato_izquierdo
    elif (verificar_candidato(candidato_derecho, arr, ini, fin)):
        return candidato_derecho
    
    return None #No habia candidato correcto.
    
def verificar_candidato(candidato, arr, ini, fin):
    if candidato is None:
        return False

    largo_tramo = fin - ini + 1
    objetivo = (largo_tramo // 2) + 1
    apariciones = 0

    for i in range(ini, fin + 1):
        if arr[i] == candidato:
            apariciones += 1
            if apariciones >= objetivo:
                return True

        restantes = fin - i  
        if apariciones + restantes < objetivo:
            return False

    return False

