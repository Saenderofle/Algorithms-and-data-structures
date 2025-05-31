def f(x):
    return x**3 + 4 * (x**2) + x - 6

def solve():
    l = 0
    r = 2
    eps = 1e-7
    m = (r + l) / 2.0

    while r - l > eps:
        if f(m) * f(l) <= 0:
            r = m
        else:
            l = m

        m = (r + l) / 2.0
    return m


if __name__ == '__main__':
    print(f"{solve():.9f}")