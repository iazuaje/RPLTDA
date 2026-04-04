from collections import deque

# pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
    if len(pedidos) == 0 : return []

    KM_INICIO_INDEX = 0
    KM_FIN_INDEX = 1

    lista_ordenada = sorted(pedidos, key=lambda rango_km: rango_km[1])
    cola = deque(lista_ordenada)
 
    candidatos = [] 
    candidatos.append(cola.popleft())

    for elemento in cola:
        if elemento[KM_INICIO_INDEX] > candidatos[-1][KM_FIN_INDEX]:
            candidatos.append(elemento)

    return candidatos