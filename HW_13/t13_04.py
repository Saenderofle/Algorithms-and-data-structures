def convert(number: str, from_base: int, to_base: int) -> str:
    decimal = 0
    for d in number:
        decimal = decimal * from_base + int(d)
    if decimal == 0:
        return "0"
    stack = []
    while decimal > 0:
        stack.append(decimal % to_base)
        decimal //= to_base
    res = ""
    while stack:
        res += get_char(stack.pop())
    return res

def get_char(n: int) -> str:
    if n < 10:
        return str(n)
    else:
        return "[" + str(n) + "]"

if __name__ == '__main__':
    A = input().strip()
    P = int(input().strip())
    print(convert(A, 10, P))
