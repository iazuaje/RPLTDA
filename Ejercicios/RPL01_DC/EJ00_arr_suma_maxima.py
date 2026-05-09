def subarreglo_cruzado(arr):
    med = len(arr) // 2

    suma_parcial = 0
    cruzado_izq = med
    suma_izq = 0
    for i in range(med - 1, -1, -1):
        suma_parcial += arr[i]
        if suma_parcial > suma_izq:
            suma_izq = suma_parcial
            cruzado_izq = i

    suma_parcial = 0
    cruzado_der = med
    suma_der = 0
    for j in range(med, len(arr)):
        suma_parcial += arr[j]
        if suma_parcial > suma_der:
            suma_der = suma_parcial
            cruzado_der = j

    return arr[cruzado_izq : cruzado_der + 1]

def max_subarray(arr):
    if len(arr) <= 1:
        return arr

    med = len(arr) // 2

    izq = max_subarray(arr[:med])
    der = max_subarray(arr[med:])
    cruzado = subarreglo_cruzado(arr)

    sumas = (sum(izq), sum(der), sum(cruzado))
    suma_maxima = max(sumas)

    if suma_maxima == sumas[0]:
        return izq
    elif suma_maxima == sumas[1]:
        return der
    else:
        return cruzado