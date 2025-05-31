def quick_sort(array):
    _sort(array, 0 , len(array) - 1)

def _sort(array, a, b):
    if a >= b:
        return

    pivot = array[a + (b - a) // 2]
    left = a
    right = b

    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left >= right:
            break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    _sort(array, a, right)
    _sort(array, right + 1, b)


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    quick_sort(array)
    print(*array)