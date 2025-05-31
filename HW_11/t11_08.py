import bisect


def merge_count_t_inversions(arr, t):
    n = len(arr)
    if n <= 1:
        return arr, 0

    mid = n // 2
    left, inv_left = merge_count_t_inversions(arr[:mid], t)
    right, inv_right = merge_count_t_inversions(arr[mid:], t)

    cross_inv = 0
    for l in left:
        pos = bisect.bisect_left(right, l - t)
        cross_inv += pos

    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])

    total_inv = inv_left + inv_right + cross_inv
    return merged, total_inv


if __name__ == '__main__':
    with open("input.txt") as f:
        header = f.readline().strip().split()
        n = int(header[0])
        t = int(header[1])
        arr = list(map(int, f.readline().strip().split()))
        _, inversions = merge_count_t_inversions(arr, t)
        print(inversions)
