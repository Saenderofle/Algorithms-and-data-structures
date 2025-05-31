def count_ways_stack(pattern, i, stack):
    if i == len(pattern):
        return 1 if not stack else 0

    ways = 0
    char = pattern[i]

    if char == '(':
        stack.append('(')
        ways = count_ways_stack(pattern, i + 1, stack)
        stack.pop()
    elif char == ')':
        if not stack:
            return 0
        top = stack.pop()
        ways = count_ways_stack(pattern, i + 1, stack)
        stack.append(top)
    elif char == '?':
        stack.append('(')
        ways = count_ways_stack(pattern, i + 1, stack)
        stack.pop()
        if stack:
            top = stack.pop()
            ways += count_ways_stack(pattern, i + 1, stack)
            stack.append(top)
    return ways % 301907


def solve():
    with open("input.txt", "r") as f:
        pattern = f.read().strip()
    result = count_ways_stack(pattern, 0, [])
    print(result)



if __name__ == '__main__':
    solve()
