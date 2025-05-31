def insertion_sort(array):
    n = len(array)
    for pos in range(1, n):
        x = array[pos]
        while pos > 0:
            if array[pos - 1] > x:
                array[pos] = array[pos - 1]
            else:
                break
            pos -= 1
        array[pos] = x
    return array

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        arr.append((a, b, c))

    array = insertion_sort(arr)
    for i in array:
        print(*i)
