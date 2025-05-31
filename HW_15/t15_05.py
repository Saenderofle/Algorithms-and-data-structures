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

    def answer_reverse(self):
        curr = self.head
        res = []

        while curr is not None:
            res.append(str(curr.item))
            curr = curr.next

        return " ".join(res[::-1])


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    linked_list = LinkedList()
    for num in arr:
        linked_list.addElement(num)
    print(linked_list.answer())
    print(linked_list.answer_reverse())
