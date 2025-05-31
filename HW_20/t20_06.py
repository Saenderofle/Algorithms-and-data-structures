class SegmentTree:
    def __init__(self, size):
        n = 1
        while n < size:
            n <<= 1
        self.n = n
        self.min_t = [10**18] * (2 * n)
        self.max_t = [-10**18] * (2 * n)

    def build(self, arr):
        for i, v in enumerate(arr):
            self.min_t[self.n + i] = v
            self.max_t[self.n + i] = v
        for i in range(self.n - 1, 0, -1):
            self.min_t[i] = min(self.min_t[2*i], self.min_t[2*i + 1])
            self.max_t[i] = max(self.max_t[2*i], self.max_t[2*i + 1])

    def update(self, pos, value):
        i = pos + self.n
        self.min_t[i] = value
        self.max_t[i] = value
        i //= 2
        while i:
            self.min_t[i] = min(self.min_t[2*i], self.min_t[2*i + 1])
            self.max_t[i] = max(self.max_t[2*i], self.max_t[2*i + 1])
            i //= 2

    def query(self, l, r):
        l += self.n
        r += self.n
        cur_min = 10**18
        cur_max = -10**18
        while l <= r:
            if l & 1:
                cur_min = min(cur_min, self.min_t[l])
                cur_max = max(cur_max, self.max_t[l])
                l += 1
            if not (r & 1):
                cur_min = min(cur_min, self.min_t[r])
                cur_max = max(cur_max, self.max_t[r])
                r -= 1
            l //= 2
            r //= 2
        return cur_min, cur_max


if __name__ == "__main__":
    k = int(input())
    N = 100_000

    a = [0] * N
    for i in range(N):
        n = i + 1
        a[i] = (n * n) % 12345 + (n * n * n) % 23456

    st = SegmentTree(N)
    st.build(a)

    results = []
    for _ in range(k):
        x, y = map(int, input().split())
        if x > 0:
            l = x - 1
            r = y - 1
            mn, mx = st.query(l, r)
            results.append(str(mx - mn))
        else:
            idx = -x - 1
            st.update(idx, y)

    print('\n'.join(results))
