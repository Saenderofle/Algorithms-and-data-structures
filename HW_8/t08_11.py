def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):

            key_j = (array[j] % 10, array[j])
            key_j1 = (array[j + 1] % 10, array[j + 1])

            if key_j > key_j1:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    print(*bubble_sort(arr))
