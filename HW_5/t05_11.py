def solve():
    R, L, B = map(int, input().split())
    x = [int(input()) for _ in range(R)]
    prefix = [0] * (R + 1)
    for i in range(R):
        prefix[i + 1] = prefix[i] + x[i]

    def can_deliver(k):
        if k == 0:
            return True
        for i in range(0, R - k + 1):
            m = i + (k - 1) // 2
            med = x[m]
            left_count = m - i
            right_count = (i + k - 1) - m
            cost_left = med * left_count - (prefix[m] - prefix[i])
            cost_right = (prefix[i + k] - prefix[m + 1]) - med * right_count
            if cost_left + cost_right <= B:
                return True
        return False

    l = 0
    r = R + 1
    while r - l > 1:
        m = (l + r) // 2
        if can_deliver(m):
            l = m
        else:
            r = m

    print(l)

if __name__ == '__main__':
    solve()
