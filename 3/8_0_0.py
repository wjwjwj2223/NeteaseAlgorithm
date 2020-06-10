class BSTNode(object):
    def __init__(self, label, left=None, right=None):
        self.left = left
        self.right = right
        self.label = label

    def setLeftNode(self, left):
        self.left = left

    def setRightNode(self, right):
        self.right = right


class BST(object):
    def __init__(self, counts):
        self.rootNode = BSTNode(ord(counts[0]))
        for i in counts:
            self.insert(ord(i))

    def insert(self, label):
        def findNode(node, label):
            if not node.left and label < node.label:
                return node
            if not node.right and label > node.label:
                return node
            if label < node.label:
                return findNode(node.left, label)
            if label > node.label:
                return findNode(node.right, label)

        node = findNode(self.rootNode, label)
        if label > node.label:
            node.right = BSTNode(label)
        elif label < node.label:
            node.left = BSTNode(label)


n_m = input().split(' ')
n = int(n_m[0])
m = int(n_m[1])

nodes = []
for a in range(0, n):
    relation = list(input())
    node = BSTNode(ord(relation[0]))
    if relation[1] != "-":
        node.left = BSTNode(ord(relation[1]))
    if relation[2] != "-":
        node.right = BSTNode(ord(relation[2]))
    nodes.append(node)


def findNode(count):
    for node in nodes:
        if node.label == count:
            return node
    return None


def find(firstNode, last, count=0):
    relFirstNode = findNode(firstNode.label)
    if not relFirstNode:
        return -1
    if relFirstNode.left.label == last or relFirstNode.right.label == last:
        count += 1
        return count
    for node in nodes:
        if node.label == relFirstNode.label:
            count += 1
            return find(node.left, last)
            return find(node.right, last)
    return -1


result = []
for a in range(0, m):
    inp = input()
    asks = list(inp)
    first = ord(asks[0])
    last = ord(asks[1])
    positive = find(BSTNode(first), last)
    flashback = find(BSTNode(last), first)
    greatString = "great-"
    if positive == -1 and flashback == -1:
        result.append("-")
        continue
    if positive != -1:
        if positive == 1:
            result.append("parent")
        elif positive == 2:
            result.append("grandparent")
        elif positive >= 3:
            count = positive - 2
            result.append(count * greatString + "grandparent")
        continue
    if flashback != -1:
        if flashback == 1:
            result.append("child")
        elif flashback == 2:
            result.append("grandchild")
        elif flashback >= 3:
            count = flashback - 2
            result.append(count * greatString + "grandchild")
        continue

for r in result:
    print(r)
