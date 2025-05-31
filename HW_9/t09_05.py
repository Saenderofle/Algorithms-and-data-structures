def merge_sort(array):
    _sort_m(array, 0, len(array) - 1)
    return array

def _sort_m(array, a, b):
    if a >= b:
        return

    m = a + (b - a) // 2
    _sort_m(array, a, m)
    _sort_m(array, m + 1, b)

    left = array[a: m + 1]

    i = 0
    j = m + 1
    k = a

    while i < len(left) and j <= b:
        if left[i][0] <= array[j][0]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = array[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

if __name__ == '__main__':
    n = int(input().strip())
    array = []

    for _ in range(n):
        x, y = map(int, input().split())
        array.append((x, y))

    sorted_array = merge_sort(array)

    for x, y in sorted_array:
        print(x, y)
