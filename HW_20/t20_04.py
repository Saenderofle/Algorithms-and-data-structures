import math

class SegmentTree:
    def __init__(self, array):
        k = len(array)
        n = 1 << math.ceil(math.log2(k)) if k > 1 else 1
        self.size = n
        self.items = [(0, 1)] * (2 * n)

        for i, v in enumerate(array):
            self.items[n + i] = (v, v)

        for i in range(n - 1, 0, -1):
            g1, l1 = self.items[2 * i]
            g2, l2 = self.items[2 * i + 1]
            g = math.gcd(g1, g2)
            l = (l1 // math.gcd(l1, l2)) * l2
            self.items[i] = (g, l)

    def update(self, pos, x):
        idx = (pos - 1) + self.size
        self.items[idx] = (x, x)
        idx //= 2
        while idx:
            g1, l1 = self.items[2 * idx]
            g2, l2 = self.items[2 * idx + 1]
            g = math.gcd(g1, g2)
            l = (l1 // math.gcd(l1, l2)) * l2
            self.items[idx] = (g, l)
            idx //= 2

    def sum(self, left, right):
        l = (left - 1) + self.size
        r = (right - 1) + self.size
        g_res = 0
        l_res = 1
        while l <= r:
            if l & 1:
                g_r, l_r = self.items[l]
                g_res = math.gcd(g_res, g_r)
                l_res = (l_res // math.gcd(l_res, l_r)) * l_r
                l += 1
            if not (r & 1):
                g_r, l_r = self.items[r]
                g_res = math.gcd(g_res, g_r)
                l_res = (l_res // math.gcd(l_res, l_r)) * l_r
                r -= 1
            l //= 2
            r //= 2
        return g_res, l_res


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    seg = SegmentTree(arr)
    out = []
    for _ in range(m):
        q, l, r = input().split()
        q = int(q)
        l = int(l)
        r = int(r)
        if q == 1:
            gcd_val, lcm_val = seg.sum(l, r)
            if gcd_val < lcm_val:
                out.append("wins")
            elif gcd_val > lcm_val:
                out.append("loser")
            else:
                out.append("draw")
        elif q == 2:
            seg.update(l, r)
    print("\n".join(out))
