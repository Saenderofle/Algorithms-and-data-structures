class Tree:
    def __init__(self, key, bribe):
        self.key = key
        self.bribe = bribe
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def compute_cost(node):
    if not node.children:
        return node.bribe
    else:
        return node.bribe + min(compute_cost(child) for child in node.children)


if __name__ == '__main__':
    n = int(input().strip())
    nodes = {i: Tree(i, 0) for i in range(1, n + 1)}
    subordinates = {}
    for i in range(1, n + 1):
        parts = input().split()
        D = int(parts[0])
        K = int(parts[1])
        nodes[i].bribe = D
        if K > 0:
            sub_list = list(map(int, parts[2 : 2+K]))
        else:
            sub_list = []
        subordinates[i] = sub_list

    for i in range(1, n + 1):
        for sub in subordinates[i]:
            nodes[i].add_child(nodes[sub])

    result = compute_cost(nodes[1])
    print(result)
