from math import sin

def solve():
    l = 1.6
    r = 3
    eps = 1e-7

    while r - l > eps:
        m = (l + r) / 2.0
        if sin(m) - (m / 3) > 0:
            l = m
        else:
            r = m
    return m

if __name__ == '__main__':
    print(solve())