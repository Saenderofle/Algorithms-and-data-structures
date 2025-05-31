def с(n, a):
    sum = 0
    for i in range(n):
        sum += a ** i                   # O(n)
    return sum

def c_optimized(n, a):
    if n == 1:
        return n                        # O(1)
    return (1 - a ** i) // (1 - a)