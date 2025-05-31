def solve(n, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        m = left + (right - left) // 2
        if arr[m] == n:
            return "YES"
        elif arr[m] < n:
            left = m + 1
        else:
            right = m - 1
    return "NO"


if __name__=='__main__':
    n = int(input())
    collection = list(map(int, input().split()))
    m = int(input())
    choice = list(map(int, input().split()))

    if len(collection) == n and len(choice) == m:
        for i in choice:
            print(solve(i, collection))
    else:
        print(ValueError("Ви не ввели достатню кількість символів"))
