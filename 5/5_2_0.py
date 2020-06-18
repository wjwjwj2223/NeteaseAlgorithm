class Node(object):

    def __init__(self, value, left=None, right=None):
        self.label = value
        self.leftNode = None
        self.rightNode = None


class BST(object):

    def __init__(self):
        self.rootNode = None

    def add(self, value):
        if not self.rootNode:
            self.rootNode = Node(value)
            return
        node = self.rootNode
        while node:
            if value < node.label:
                if node.leftNode:
                    node = node.leftNode
                else:
                    break
            elif value > node.label:
                if node.rightNode:
                    node = node.rightNode
                else:
                    break
            else:
                return

        if value < node.label:
            node.leftNode = Node(value)
        elif value > node.label:
            node.rightNode = Node(value)

    def formatPrint(self):
        self.prePrint(self.rootNode)

    def prePrint(self, node, count=0):
        if not node:
            return
        s = ''
        for c in range(0, count*2):
            s += ' '
        print(s + str(node.label))
        count += 1
        self.prePrint(node.leftNode, count)
        self.prePrint(node.rightNode, count)


s_list = input().split(' ')
bst = BST()
for s in s_list:
    bst.add(int(s))
bst.formatPrint()
