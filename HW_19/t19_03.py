n = int(input())
a = list(map(int, input().split()))

a = [0] + a
is_heap = True

for i in range(1, n+1):
    if 2 * i <= n and a[i] > a [2 * i]:
        is_heap = False
        break
    if 2 * i + 1 <= n and a[i] > a[2*i +1]:
        is_heap = False
        break
print("YES" if is_heap else "NO")