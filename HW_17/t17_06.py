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
                if key == node.key:
                    break
                elif key < node.key:
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

    def pre_order(self):
        result = ""
        if not self.empty():
            result += self.item()
            if self.hasLeft():
                result += self.leftChild().pre_order()
            if self.hasRight():
                result += self.rightChild().pre_order()
        return result


if __name__ == '__main__':
    rounds = []
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line == '*':
            break
        if line:
            rounds.append(line)
    if rounds:
        rounds.reverse()
        root_letter = rounds[0][0]
        tree = SearchTree(root_letter)
        for round_letters in rounds[1:]:
            for ch in round_letters:
                tree.insert(ch)
        print(tree.pre_order())
