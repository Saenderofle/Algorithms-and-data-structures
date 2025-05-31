class Graph:
    def __init__(self, oriented = False, vertex_number = 0):
        self.oriented = oriented
        self.vertex_number = vertex_number
        self.in_deg = [0] * vertex_number
        self.out_deg = [0] * vertex_number


    def addEdge(self, s, d, w = 1):
        self.out_deg[s] += w
        self.in_deg[d] += w

        if not self.oriented:
            self.out_deg[d] += w
            self.in_deg[s] += w


    def degrees(self):
        return self.in_deg, self.out_deg


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(True, n)

    for i in range(m):
        u, v = map(int, input().split())
        g.addEdge(u - 1, v - 1)

    in_deg, out_deg = g.degrees()
    for i in range(n):
        print(in_deg[i], out_deg[i])

