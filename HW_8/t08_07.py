def insertion_sort(array):
    n = len(array)
    for pos in range(1, n):
        x = array[pos]
        _sorted = False
        while pos > 0:
            if array[pos - 1] > x:
                array[pos] = array[pos - 1]
                _sorted = True
            else:
                break
            pos -= 1
        array[pos] = x
        if _sorted:
            print(" ".join(map(str, array)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    insertion_sort(arr)