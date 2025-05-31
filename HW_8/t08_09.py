def weight_num(num):
    return sum(map(int, str(num)))

def key(num):
    return (weight_num(num), str(num))

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if key(array[j]) > key(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

    return array
if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())

    arr = list(range(1, n + 1))

    _sorted = bubble_sort(arr)

    pos = _sorted.index(k) + 1
    k_el = _sorted[k - 1]

    print(pos)
    print(k_el)