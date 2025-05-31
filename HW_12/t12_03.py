class Stack:
    def __init__(self, maxSize = 100):
        self.items = [0 for _ in range(maxSize)]
        self._top = -1


    def push(self, item):
        self._top += 1
        self.items[self._top] = item
        return 'ok'

    def pop(self):
        if self._top < 0:
            return 'error'
        item = self.items[self._top]
        self._top -= 1
        return item

    def size(self):
        return self._top + 1

    def back(self):
        if self._top < 0:
            return 'error'
        return self.items[self._top]

    def clear(self):
        self.__init__(len(self.items))
        return 'ok'

    def exit(self):
        return 'bye'

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == 'bye':
                break



