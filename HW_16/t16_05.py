class Tree:
    def __init__(self, key):
        self.key = key
        self.children = {}

    def add_path(self, parts):
        if not parts:
            return
        first = parts[0]
        if first not in self.children:
            self.children[first] = Tree(first)
        self.children[first].add_path(parts[1:])

    def print_tree(self, depth=0):
        if self.key != "":
            print(" " * depth + self.key)
        for key in sorted(self.children.keys()):
            self.children[key].print_tree(depth + 1)


if __name__ == '__main__':
    n = int(input().strip())
    root = Tree("")

    for _ in range(n):
        path = input().strip()
        parts = path.split("\\")
        root.add_path(parts)

    for key in sorted(root.children.keys()):
        root.children[key].print_tree(0)
