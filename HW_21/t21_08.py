class Graph:
    def __init__(self, oriented=True, v=0):
        self.oriented = oriented
        self.v = v
        self.graph = [[0] * v for _ in range(v)]

    def addEdge(self, s, d, w=1):
        self.graph[s][d] += w
        if not self.oriented:
            self.graph[d][s] += w

    def multiEdges(self):
        for i in range(self.v):
            for j in range(self.v):
                if self.graph[i][j] > 1:
                    return True
        return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(oriented=True, v=n)

    for _ in range(m):
        u, v = map(int, input().split())
        g.addEdge(u - 1, v - 1)

    print("YES" if g.multiEdges() else "NO")