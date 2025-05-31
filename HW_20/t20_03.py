from math import log2, gcd

class SegmentTree:
    def __init__(self, array):
        k = len(array)
        if k == 1:
            n = 1
        else:
            n = 1 << (int(log2(k - 1)) + 1)

        self.mItems = 2 * n * [0]

        for i in range(k):
            self.mItems[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.mItems[i] = gcd(self.mItems[2 * i], self.mItems[2 * i + 1])

        self.mSize = n

    def update(self, pos, x):
        pos += self.mSize
        self.mItems[pos] = x

        i = pos // 2
        while i > 0:
            self.mItems[i] = gcd(self.mItems[2 * i], self.mItems[2 * i + 1])
            i //= 2

    def sum(self, l, r):
        l += self.mSize
        r += self.mSize

        res = 0
        while l <= r:
            if l & 1:
                res = gcd(res, self.mItems[l])
                l += 1
            if not (r & 1):
                res = gcd(res, self.mItems[r])
                r -= 1
            l //= 2
            r //= 2
        return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    seg = SegmentTree(arr)

    for _ in range(q):
        parts = input().split()
        operation = parts[0]
        l = int(parts[1]) - 1
        r = int(parts[2]) - 1
        if operation == '1':
            print(seg.sum(l, r))
        else:
            seg.update(l, r + 1)
