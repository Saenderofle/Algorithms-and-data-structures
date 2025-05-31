class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addElement(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def answer(self):
        curr = self.head
        res = []
        while curr is not None:
            res.append(str(curr.item))
            curr = curr.next
        return " ".join(res)

    def RotateRight(self, k):
        if self.head is None or self.head.next is None:
            return
        # Обчислюємо довжину списку
        n = 0
        curr = self.head
        while curr:
            n += 1
            curr = curr.next
        k %= n
        if k == 0:
            return
        # Знаходимо новий tail: (n - k - 1)-й вузол (0-індексований)
        curr = self.head
        for _ in range(n - k - 1):
            curr = curr.next
        new_tail = curr
        new_head = curr.next
        # Робимо зв'язок: хвіст списку вказує на head для утворення кола
        self.tail.next = self.head
        # Перериваємо коло: новий tail стає останнім вузлом
        new_tail.next = None
        self.head = new_head
        self.tail = new_tail


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    linked_list = LinkedList()
    for num in arr:
        linked_list.addElement(num)
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line == "":
            continue
        k = int(line)
        linked_list.RotateRight(k)
        print(linked_list.answer())
