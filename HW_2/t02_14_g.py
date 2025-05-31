def g(n, a):
    sum = 1
    fact = 1
    power_ai = 1
    for i in range(1, n + 1):
        fact *= i
        power_ai *= a
        sum *= power_ai / (1 + fact)

    return sum