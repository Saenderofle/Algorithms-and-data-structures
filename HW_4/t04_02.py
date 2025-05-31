from math import sqrt

def solve(c):
    l = 0
    r = 1e10
    eps = 1e-7
    m = (r + l) / 2.0

    while r - l > eps:
        if m ** 2 + sqrt(m) < c:
            l = m
        else:
            r = m
        m = (r + l) / 2.0
    return m

if __name__ == '__main__':
    c = float(input())

    result = solve(c)
    print(f"{result:.9f}")