def h(n, m):
    sum = 1
    for i in range(1, n + 1):
        sum *= 1 / (1 + i ** m)

    return sum