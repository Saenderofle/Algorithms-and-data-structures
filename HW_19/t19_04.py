class Heap:
    def __init__(self):
        self.heap = [None]
        self.size = 0
        self.index = {}


    def _add(self, id, priority):
        self.size += 1
        self.heap.append([priority, id])
        self.index[id] = self.size
        self.siftUp(self.size)

    def _pop(self):
        top = self.heap[1]
        self.index.pop(top[1])

        if self.size == 1:
            self.heap.pop()
            self.size -= 1
            return top

        self.heap[1] = self.heap[self.size]
        self.index[self.heap[1][1]] = 1
        self.heap.pop()
        self.size -= 1
        self.siftDown(1)
        return top

    def _change(self, id, new_priority):
        idx = self.index.get(id)

        if idx is None:
            return

        old_priority = self.heap[idx][0]
        self.heap[idx][0] = new_priority

        if new_priority > old_priority:
            self.siftUp(idx)
        elif new_priority < old_priority:
            self.siftDown(idx)

    def siftUp(self, i):
        while i > 1:
            parent = i // 2
            if self.heap[i][0] > self.heap[parent][0]:
                self.swap(i, parent)
            else:
                break
            i = parent

    def siftDown(self, i):
        while 2 * i  <= self.size:
            left = 2 * i
            right = left + 1
            max_child = left

            if right <= self.size and self.heap[right][0] > self.heap[left][0]:
                max_child = right
            if self.heap[i][0] < self.heap[max_child][0]:
                self.swap(i, max_child)
                i = max_child
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.index[self.heap[i][1]] = i
        self.index[self.heap[j][1]] = j


if __name__ == '__main__':
    heap = Heap()
    res = []

    try:
        while True:
            line = input().strip()

            if not line:
                continue

            parts = line.split()
            operation = parts[0]

            if operation == 'ADD':
                id = parts[1]
                priority = int(parts[2])
                heap._add(id, priority)

            elif operation == 'POP':
                poped = heap._pop()
                res.append(f'{poped[1]} {poped[0]}')

            elif operation == 'CHANGE':
                id = parts[1]
                new_priority = int(parts[2])
                heap._change(id, new_priority)

    except EOFError:
        pass

    for result in res:
        print(result)
