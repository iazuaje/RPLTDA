def es_par(n):
    return n % 2 == 0

def operaciones(k):

    dp = []
    prev = []
    op = []

    for i in range(k + 1):
        dp.append(i)
        prev.append(i)
        op.append(i)

    for n in range(1,k + 1):
        dp[n] = dp[n-1] + 1
        prev[n] = n-1
        op[n] = "mas1"

        if es_par(n) and dp[n//2] + 1 < dp[n]:
            dp[n] = dp[n//2] + 1
            prev[n] = n//2
            op[n] = "por2"
    
    res = []
    actual = k
    while actual > 0:
        res.append(op[actual])
        actual = prev[actual]

    res.reverse()
    return res