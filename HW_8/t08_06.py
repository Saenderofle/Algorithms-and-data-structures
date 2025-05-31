def sort(array):
    n = len(array)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array



if __name__ == "__main__":
    n = int(input())
    arr = [input() for _ in range(n)]

    array = sort(arr)
    for i in array:
        print(i, end="\n")