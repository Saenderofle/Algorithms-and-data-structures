class Stack:
    def __init__(self, maxSize = 1000):
        self.items = [0 for _ in range(maxSize)]
        self._top = -1


    def push(self, item):
        self._top += 1
        self.items[self._top] = item
        return 'ok'

    def pop(self):
        item = self.items[self._top]
        self._top -= 1
        return item

    def back(self):
        return self.items[self._top]

    def size(self):
        return self._top + 1

    def clear(self):
        self.__init__(len(self.items))
        return 'ok'

    def exit(self):
        return 'bye'

    def execute(self, command):
        method, *args = command.strip()
        return getattr(self, method)(*args)


def solve(n, desired):
    station = Stack(maxSize = n + 5)
    next_in = 1
    for needed in desired:
        while next_in <= n and (station.size() == 0 or station.back() != needed):
            station.push(next_in)
            next_in += 1
        if station.back() == needed:
            station.pop()
        else:
            return False
    return True




if __name__ == '__main__':
    with open("input.txt") as f:
        lines = [line.strip() for line in f if line.strip()]
        index = 0
        while index < len(lines):
            n = int(lines[index])
            index += 1
            if n == 0:
                break
            while True:
                if index >= len(lines):
                    break

                line = lines[index]
                index += 1
                if line == '0':
                    print()
                    break
                desired = list(map(int, line.split()))
                print('Yes' if solve(n, desired) else 'No')
