INF = float('inf')

def Bellman_Ford(n, m, edges, s, f):
    dist = [INF for _ in range(n + 1)]
    used = [-1 for _ in range(n + 1)]

    dist[s] = 0

    for _ in range(n - 1):
        updated = False
        for b, e, w in edges:
            if dist[b] + w < dist[e]:
                dist[e] = dist[b] + w
                used[e] = b
                updated = True
        if not updated:
            break


    if dist[f] == INF:
        return -1

    path = []
    cur = f
    while cur != -1:
        path.append(cur)
        if cur == s:
            break
        cur = used[cur]
    path.reverse()

    return dist[f], path




if __name__ == '__main__':
    n, m = map(int, input().split())
    s, f = map(int, input().split())
    s -= 1
    f -= 1

    edges = []
    for _ in range(m):
        b, e, w = map(int, input().split())
        b -= 1
        e -= 1
        edges.append((b, e, w))
        edges.append((e, b, w))

    res = Bellman_Ford(n, m, edges, s, f)

    if res == -1:
        print(-1)
    else:
        dist, path = res
        print(dist)
        for i in range(len(path)):
            path[i] += 1
        print(*path)


