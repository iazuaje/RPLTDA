def parte_entera_raiz(n):
    return _parte_entera_raiz(n, 0, n)

def _parte_entera_raiz(numero, inicio, fin):
    if (inicio > fin):
        return fin
    mitad = (inicio + fin) // 2
    potencia = mitad * mitad
    if potencia == numero:
        return mitad
    elif potencia < numero:
        return _parte_entera_raiz(numero, mitad + 1, fin)
    else:
        return _parte_entera_raiz(numero, inicio, mitad - 1)
    