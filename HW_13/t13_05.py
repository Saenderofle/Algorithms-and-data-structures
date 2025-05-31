BRACKETS = {"(": ")", "[": "]", "{": "}"}

def check(sequence: str) -> bool:
    stack = []
    for bracket in sequence:
        if bracket in BRACKETS:
            stack.append(bracket)
        else:
            if not stack or BRACKETS[stack.pop()] != bracket:
                return False
    return not stack

if __name__ == '__main__':
    sequence = input().strip()
    print("yes" if check(sequence) else "no")
