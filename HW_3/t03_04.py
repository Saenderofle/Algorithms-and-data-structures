def max_value(n):
    bin_n = bin(n)[2::]
    max_value = n

    for i in range(len(bin_n) - 1):
        bin_n = bin_n[1:] + bin_n[0]
        max_value = max(max_value, int(bin_n, 2))

    return max_value

n = int(input())
print(max_value(n))