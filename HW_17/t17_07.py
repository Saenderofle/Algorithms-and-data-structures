class SearchTree:
    def __init__(self, key=None):
        self.key = key
        self.mLeftChild = None
        self.mRightChild = None

    def empty(self):
        return self.key is None

    def setNode(self, item):
        self.key = item

    def item(self):
        if self.empty():
            raise Exception("SearchTree: дерево порожнє")
        return self.key

    def hasLeft(self):
        return self.mLeftChild is not None

    def hasRight(self):
        return self.mRightChild is not None

    def leftChild(self):
        return self.mLeftChild

    def rightChild(self):
        return self.mRightChild

    def insert(self, key):
        if self.empty():
            self.setNode(key)
        else:
            node = self
            while True:
                if key < node.key:
                    if node.hasLeft():
                        node = node.mLeftChild
                    else:
                        node.mLeftChild = SearchTree(key)
                        break
                else:
                    if node.hasRight():
                        node = node.mRightChild
                    else:
                        node.mRightChild = SearchTree(key)
                        break

    def isSameTree(self, other):
        if self.empty() and (other is None or other.empty()):
            return 1

        if self.empty() or other is None or other.empty():
            return 0

        if self.key != other.key:
            return 0

        if self.hasLeft() and other.hasLeft():
            left_same = self.leftChild().isSameTree(other.leftChild())
        elif not self.hasLeft() and not other.hasLeft():
            left_same = 1
        else:
            left_same = 0

        if self.hasRight() and other.hasRight():
            right_same = self.rightChild().isSameTree(other.rightChild())
        elif not self.hasRight() and not other.hasRight():
            right_same = 1
        else:
            right_same = 0
        return 1 if left_same and right_same else 0


if __name__ == '__main__':
    n = int(input().strip())
    arr1 = list(map(int, input().split()))
    tree1 = SearchTree()
    for val in arr1:
        tree1.insert(val)

    m = int(input().strip())
    arr2 = list(map(int, input().split()))
    tree2 = SearchTree()
    for val in arr2:
        tree2.insert(val)

    print(tree1.isSameTree(tree2))
