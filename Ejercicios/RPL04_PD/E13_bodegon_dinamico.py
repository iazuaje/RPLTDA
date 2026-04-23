def bodegon_dinamico(P, W):
    n = len(P)

    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        grupo = P[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]

            if grupo <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - grupo] + grupo)

    seleccion = []
    w = W
    i = n

    while i > 0 and w >= 0:
        if dp[i][w] != dp[i - 1][w]:
            seleccion.append(P[i - 1])
            w -= P[i - 1]
        i -= 1

    seleccion.reverse()
    return seleccion