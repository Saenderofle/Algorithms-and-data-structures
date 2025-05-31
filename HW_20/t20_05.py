class SegmentTree:
    def __init__(self, size):
        n = 1
        while n < size:
            n <<= 1
        self.n = n
        self.tree = [0] * (2 * n)
        self.lazy = [0] * (2 * n)

    def _push(self, idx, l, r):
        if self.lazy[idx] != 0:
            self.tree[idx] += (r - l + 1) * self.lazy[idx]
            if idx < self.n:
                self.lazy[2*idx]     += self.lazy[idx]
                self.lazy[2*idx + 1] += self.lazy[idx]
            self.lazy[idx] = 0

    def _update(self, idx, l, r, ql, qr, val):
        self._push(idx, l, r)
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.lazy[idx] += val
            self._push(idx, l, r)
            return
        mid = (l + r) // 2
        self._update(2*idx, l, mid, ql, qr, val)
        self._update(2*idx + 1, mid+1, r, ql, qr, val)
        self.tree[idx] = self.tree[2*idx] + self.tree[2*idx + 1]

    def update_range(self, left, right, value):
        self._update(1, 0, self.n - 1, left, right, value)

    def _query(self, idx, l, r, ql, qr):
        self._push(idx, l, r)
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[idx]
        mid = (l + r) // 2
        return (self._query(2*idx,     l,   mid, ql, qr) +
                self._query(2*idx + 1, mid+1, r,   ql, qr))

    def query_range(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)


if __name__ == "__main__":
    q, L, R, p = map(int, input().split())
    st = SegmentTree(256)

    st.update_range(L, R, 1)

    for _ in range(1, q):
        s = st.query_range(L, R)
        L = s % p
        R = 255 - L
        st.update_range(L, R, 1)

    print(st.query_range(0, 255))

