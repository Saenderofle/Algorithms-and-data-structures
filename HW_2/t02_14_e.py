def e(n):
    sum = 1
    for i in range(1, n + 1):
        sum  *= 1 / (1 + i)

    return sum