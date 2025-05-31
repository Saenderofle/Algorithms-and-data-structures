def f(x):
    return x**3 + x + 1

def solve():
    l = 0
    r = 10
    eps = 1e-7

    while r - l > eps:
        m = (r + l) / 2.0
        if f(m) > 5:
            r = m
        else:
            l = m
    return l

if __name__ == '__main__':
    result = solve()
    print(result)