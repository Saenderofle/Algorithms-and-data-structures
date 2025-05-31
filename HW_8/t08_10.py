def parse(grade: str):
    number = grade[:-1]
    letter = grade[-1]
    return (int(number), letter)

def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if array[j] < array[min_pos]:
                min_pos = j
        array[i], array[min_pos] = array[min_pos], array[i]

    return array

if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):

        surname = input().strip()
        name = input().strip()
        grade = input().strip()
        birth_day = input().strip()

        parsed = parse(grade)
        arr.append((parsed, surname, name, birth_day, grade))

    array = selection_sort(arr)
    for i in array:
        _, surname, name, birth_day, grade = i
        print(grade, surname, name, birth_day)