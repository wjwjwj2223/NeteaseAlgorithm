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
        for i in counts:
            self.insert(int(i))

    def insert(self, label):
        def findNode(node, label):
            if not node.right and label > node.label:
                return node
            if label > node.label:
                return findNode(node.right, label)
            return None
        node = findNode(self.rootNode, label)
        if not node:
            return
        node.right = BSTNode(label)


    def printRightTree(self):
        node = self.rootNode
        string = str(node.label)
        while node.right:
            string = string + "->" + str(node.right.label)
            node = node.right
        print(string)


list_s = input()
s = list_s.split(' ')
bst = BST(s)
bst.printRightTree()
