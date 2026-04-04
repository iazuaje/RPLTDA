def bolsas(capacidad, productos):
    productos_ordenados = sorted(productos, reverse=True)
    bolsas = []

    for producto_peso in productos_ordenados:
        colocado = False

        for bolsa in bolsas:
            if sum(bolsa) + producto_peso <= capacidad:
                bolsa.append(producto_peso)
                colocado = True
                break

        if not colocado:
            bolsas.append([producto_peso])

    return bolsas