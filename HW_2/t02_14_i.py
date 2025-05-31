def i(n):
    sum = 1
    for i in range(1, n + 1):
        power_ii = i ** i
        sum *= 1 / (1 + i * power_ii)

    return sum