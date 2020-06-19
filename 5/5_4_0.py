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

    def findSum(self, number):
        def sumNode(node, accumulation):
            if accumulation == number:
                return True
            if not node:
                return False
            accumulation += node.label
            return sumNode(node.leftNode, accumulation) or sumNode(node.rightNode, accumulation)
        return sumNode(self.rootNode, 0)


s_list = input().split(' ')
bst = BST()
for s in s_list:
    bst.add(int(s))
sum = int(input())
print(bst.findSum(sum))
