INF = float('inf')


def Dextry(n, matrix, s, f):
    dist = [INF for _ in range(n)]
    used = [False for _ in range(n)]

    dist[s] = 0

    for _ in range(n):
        u = -1
        best = INF
        for i in range(n):
            if not used[i] and dist[i] < best:
                best = dist[i]
                u = i

        if u == -1 or best == INF:
            break
        used[u] = True

        for v in range(n):
            w = matrix[u][v]
            if w >= 0 and not used[v]:
                nd = dist[u] + w
                if nd < dist[v]:
                    dist[v] = nd

    return dist[f] if dist[f] < INF else -1



if __name__ == '__main__':
    n, s, f = map(int,input().split())
    s -= 1
    f -= 1

    matrix = [list(map(int, input().split())) for _ in range(n)]

    print(Dextry(n, matrix, s, f))

