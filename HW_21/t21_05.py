class Graph:
    def __init__(self, oriented = False, vertex_number = 20):
        self.oriented = oriented
        self.vertex_number = vertex_number
        self.graph = [[0] * vertex_number for _ in range(vertex_number)]


    def isHanging(self):
        counter = 0
        for i in range(self.vertex_number):
            if sum(self.graph[i]) == 1:
                counter += 1

        return counter



if __name__ == '__main__':
    n = int(input())
    g = Graph(oriented=False, vertex_number = n)

    for i in range(n):
        g.graph[i] = list(map(int, input().split()))

    res = g.isHanging()
    print(res)
