import sys
sys.set_int_max_str_digits(10**6)

def karatsuba(x, y):
    if x == "0" or y == "0":
        return "0"

    if len(x) <= 64 and len(y) <= 64:
        return str(int(x) * int(y))

    n = max(len(x), len(y))

    if n % 2 != 0:
        n += 1
    x = x.zfill(n)
    y = y.zfill(n)

    m = n // 2

    a, b = x[:-m], x[-m:]
    c, d = y[:-m], y[-m:]

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)

    a_p_b = str(int(a) + int(b))
    c_p_d = str(int(c) + int(d))

    ab_p_cd = karatsuba(a_p_b, c_p_d)

    ab_p_cd = str(int(ab_p_cd) - int(ac) - int(bd))

    result = int(ac) * 10 ** (2*m) + int(ab_p_cd) * 10 ** (m) + int(bd)
    return str(result)

if __name__ == '__main__':
    with open("input.txt") as f:
        for line in f:
            data = line.split()
            A = data[0]
            B = data[1]
            result = karatsuba(A,B)
            print(result)

        f.close()
