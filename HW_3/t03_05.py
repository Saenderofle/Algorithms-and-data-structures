def solve(arr, a, b):
    count = 0
    for i in arr:
        if a <= i <= b:
            count += 1
    return count


if __name__ == '__main__':
    f = open('t03_05.txt')
    while f.readline():
        arr = [int(x) for x in f.readline().split()]
        a, b = [int(x) for x in f.readline().split()]
        print(solve(arr, a, b))
    f.close()
