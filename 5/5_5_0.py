class Node(object):

    def __init__(self, value, left=None, right=None):
        self.label = value
        self.parent = None
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
            node.leftNode.parent = node
        elif value > node.label:
            node.rightNode = Node(value)
            node.rightNode.parent = node

    def prePrint(self, node):
        if not node:
            return
        print(str(node.label), end=' ')
        self.prePrint(node.leftNode)
        self.prePrint(node.rightNode)

    def union(self, bst):

        def sum(node1Parent, node1, node2, left):
            if not node2:
                return
            if not node1:
                if left:
                    node1Parent.leftNode = Node(node2.label)
                    sum(node1Parent.leftNode, None, node2.leftNode, True)
                    sum(node1Parent.leftNode, None, node2.rightNode, False)
                else:
                    node1Parent.rightNode = Node(node2.label)
                    sum(node1Parent.rightNode, None, node2.leftNode, True)
                    sum(node1Parent.rightNode, None, node2.rightNode, False)
                return
            node1.label = node1.label + node2.label
            sum(node1, node1.leftNode, node2.leftNode, True)
            sum(node1, node1.rightNode, node2.rightNode, False)

        sum(self.rootNode.parent, self.rootNode, bst.rootNode, None)


s1_list = input().split(' ')
s2_list = input().split(' ')
bst1 = BST()
bst2 = BST()
for s in s1_list:
    bst1.add(int(s))
for s in s2_list:
    bst2.add(int(s))
bst1.union(bst2)
bst1.prePrint(bst1.rootNode)
