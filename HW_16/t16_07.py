mod = 1000000007
base = 33

class Tree:
    def __init__(self, n, parents):
        self.n = n
        self.parent = [-1] * n
        for i in range(1, n):
            self.parent[i] = parents[i - 1]
        self.children = [[] for _ in range(n)]
        for i in range(1, n):
            p = self.parent[i]
            self.children[p].append(i)
        self.depth = [0] * n
        self.LOG = 0
        self.up = None

    def preprocess(self):
        from collections import deque
        q = deque([0])
        while q:
            u = q.popleft()
            for v in self.children[u]:
                self.depth[v] = self.depth[u] + 1
                q.append(v)
        self.LOG = 0
        while (1 << self.LOG) <= self.n:
            self.LOG += 1
        self.up = [[-1] * self.n for _ in range(self.LOG)]
        for i in range(self.n):
            self.up[0][i] = self.parent[i]
        for j in range(1, self.LOG):
            for i in range(self.n):
                if self.up[j - 1][i] != -1:
                    self.up[j][i] = self.up[j - 1][self.up[j - 1][i]]
                else:
                    self.up[j][i] = -1

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        bit = 0
        while diff:
            if diff & 1:
                u = self.up[bit][u]
            diff //= 2
            bit += 1
        if u == v:
            return u
        for j in range(self.LOG - 1, -1, -1):
            if self.up[j][u] != self.up[j][v]:
                u = self.up[j][u]
                v = self.up[j][v]
        return self.parent[u]

if __name__ == '__main__':
    data = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "":
            continue
        data.append(line.strip())
    if not data:
        exit()
    n, m = map(int, data[0].split())
    if n > 1:
        parents = list(map(int, data[1].split()))
    else:
        parents = []
    a1, a2 = map(int, data[2].split())
    x, y, z = map(int, data[3].split())
    tree = Tree(n, parents)
    tree.preprocess()
    a = [0] * (2 * m + 1)
    a[1] = a1
    a[2] = a2
    for i in range(3, 2 * m + 1):
        a[i] = (x * a[i - 2] + y * a[i - 1] + z) % n
    total = 0
    u = a[1]
    v = a[2]
    ans = tree.lca(u, v)
    total += ans
    prev = ans
    for i in range(2, m + 1):
        u = (a[2 * i - 1] + prev) % n
        v = a[2 * i]
        ans = tree.lca(u, v)
        total += ans
        prev = ans
    print(total)