n, m, p = map(int, input().split())
danger_input = list(map(int, input().split()))
is_danger = [False] * (n + 1)
for d in danger_input:
    is_danger[d] = True

edges = []
for _ in range(m):
    x, y, l = map(int, input().split())
    edges.append((l, x, y))

parent = list(range(n + 1))
rank = [0] * (n + 1)

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root == v_root:
        return False
    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    else:
        parent[v_root] = u_root
        if rank[u_root] == rank[v_root]:
            rank[u_root] += 1
    return True

deg = [0] * (n + 1)
edges.sort()
cost = 0
components = n

for l, u, v in edges:
    if is_danger[u] and deg[u] == 1:
        continue
    if is_danger[v] and deg[v] == 1:
        continue
    if union(u, v):
        cost += l
        components -= 1
        if is_danger[u]:
            deg[u] += 1
        if is_danger[v]:
            deg[v] += 1
        if components == 1:
            break

if components == 1:
    print(cost)
else:
    print("impossible")
