def bubble_sort(array: list):
    counter = 0
    n = len(array)
    for j in range(n - 1, 0 , -1):
        for i in range(j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                counter += 1

    return counter

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    print(bubble_sort(arr))