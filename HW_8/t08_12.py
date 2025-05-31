def selection_sort(array):
    n = len(array)
    f = array[0]
    counter = 0

    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if array[j] < array[pos]:
                pos = j

        if pos != i:
            if array[i] == f or array[pos] == f:
                counter += 1
        array[i], array[pos] = array[pos], array[i]

    return counter

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(selection_sort(arr))