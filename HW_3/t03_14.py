def search_rightmost(array, x):
    l, r = 0, len(array)
    while l < r:
        m = (l + r) // 2
        if array[m] <= x:
            l = m + 1
        else:
            r = m
    if l > 0 and array[l - 1] == x:
        return l
    return 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    x = int(input())
    print(search_rightmost(arr, x))
