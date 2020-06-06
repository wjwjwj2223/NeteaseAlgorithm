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
        self.rootNode = BSTNode(int(counts[0]))
        self.countSize = 1
        for i in counts:
            self.insert(int(i))

    def insert(self, label):
        def findNode(node, label):
            if node.label == label:
                return None
            if not node.left and label < node.label:
                return node
            if not node.right and label > node.label:
                return node
            if label < node.label:
                return findNode(node.left, label)
            if label > node.label:
                return findNode(node.right, label)

        node = findNode(self.rootNode, label)
        if not node:
            return
        if label > node.label:
            node.right = BSTNode(label)
        elif label < node.label:
            node.left = BSTNode(label)
        self.countSize += 1


list_s = input()
s = list_s.split(' ')
bst = BST(s)
print(bst.countSize)
