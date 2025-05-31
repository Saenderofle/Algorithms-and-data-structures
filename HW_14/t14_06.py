class Deque:
    def __init__(self, capacity=4):
        self._items = [None] * capacity
        self._front = 0
        self._size = 0

    def _resize(self, new_capacity):
        new_items = [None] * new_capacity
        for i in range(self._size):
            new_items[i] = self._items[(self._front + i) % len(self._items)]
        self._items = new_items
        self._front = 0

    def push_back(self, item):
        if self._size == len(self._items):
            self._resize(len(self._items) * 2)
        back = (self._front + self._size) % len(self._items)
        self._items[back] = item
        self._size += 1
        return "ok"

    def push_front(self, item):
        if self._size == len(self._items):
            self._resize(len(self._items) * 2)
        self._front = (self._front - 1) % len(self._items)
        self._items[self._front] = item
        self._size += 1
        return "ok"

    def pop_front(self):
        if self._size == 0:
            return "error"
        item = self._items[self._front]
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        return item

    def pop_back(self):
        if self._size == 0:
            return "error"
        back = (self._front + self._size - 1) % len(self._items)
        item = self._items[back]
        self._size -= 1
        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._items[self._front]

    def back(self):
        if self._size == 0:
            return "error"
        back = (self._front + self._size - 1) % len(self._items)
        return self._items[back]

    def size(self):
        return self._size

    def clear(self):
        self._items = [None] * 4
        self._front = 0
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]
        if args:
            args = [int(x) if x.lstrip("-").isdigit() else x for x in args]
        return getattr(self, cmd)(*args)

if __name__ == '__main__':
    deque = Deque()
    with open("input.txt", "r") as f:
        for line in f:
            res = deque.execute(line.strip())
            print(res)
            if res == "bye":
                break
