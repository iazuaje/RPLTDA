def resolver_lineal(ganancias, inicio, fin):
    cantidad = fin - inicio
    if cantidad <= 0:
        return []

    dp = [0] * (cantidad + 1)
    elegidos = [False] * (cantidad + 1)

    for i in range(1, cantidad + 1):
        ganancia_actual = ganancias[inicio + i - 1]
        tomar = ganancia_actual
        if i >= 2:
            tomar += dp[i - 2]

        no_tomar = dp[i - 1]

        if tomar > no_tomar:
            dp[i] = tomar
            elegidos[i] = True
        else:
            dp[i] = no_tomar

    seleccion = []
    i = cantidad
    while i > 0:
        if elegidos[i]:
            seleccion.append(inicio + i - 1)
            i -= 2
        else:
            i -= 1

    seleccion.reverse()
    return seleccion


def lunatico(ganancias):
    n = len(ganancias)

    if n == 0:
        return []
    if n == 1:
        return [0] if ganancias[0] > 0 else []

    opcion_sin_ultima = resolver_lineal(ganancias, 0, n - 1)
    opcion_sin_primera = resolver_lineal(ganancias, 1, n)

    ganancia_sin_ultima = sum(ganancias[i] for i in opcion_sin_ultima)
    ganancia_sin_primera = sum(ganancias[i] for i in opcion_sin_primera)

    if ganancia_sin_ultima >= ganancia_sin_primera:
        return opcion_sin_ultima
    return opcion_sin_primera