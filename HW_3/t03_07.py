def lower(n, arr):
    left = 0
    right = len(arr)
    while left < right:
        m = left + (right - left) // 2
        if arr[m] < n:
            left = m + 1
        else:
            right = m
    return  left

def upper(n, arr):
    left = 0
    right = len(arr)
    while left < right:
        m = left + (right - left) // 2
        if arr[m] <= n:
            left = m + 1
        else:
            right = m
    return  left


if __name__ == '__main__':
    n = int(input())
    collection = list(map(int, input().split()))
    m = int(input())
    choice = list(map(int, input().split()))

    if len(collection) == n and len(choice) == m:
        for i in choice:
            print(upper(i, collection) - lower(i, collection))
    else:
        print(ValueError("Не коректно введені дані"))