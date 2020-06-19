class Node(object):

    def __init__(self, value, left=None, right=None):
        self.label = value
        self.level = 0
        self.parent = None
        self.leftNode = None
        self.rightNode = None


class BST(object):

    def __init__(self):
        self.rootNode = None

    def add(self, value):
        if not self.rootNode:
            self.rootNode = Node(value)
            self.rootNode.level = 0
            return
        node = self.rootNode
        height = 1
        while node:
            if value < node.label:
                if node.leftNode:
                    node = node.leftNode
                    height += 1
                else:
                    break
            elif value > node.label:
                if node.rightNode:
                    node = node.rightNode
                    height += 1
                else:
                    break
            else:
                return

        if value < node.label:
            node.leftNode = Node(value)
            node.leftNode.parent = node
            node.leftNode.level = height
        elif value > node.label:
            node.rightNode = Node(value)
            node.rightNode.parent = node
            node.rightNode.level = height

    def prePrint(self, node):
        if not node:
            return
        print(str(node.label))
        self.prePrint(node.leftNode)
        self.prePrint(node.rightNode)

    def midPrint(self, node):
        if not node:
            return
        self.midPrint(node.leftNode)
        print(str(node.label))
        self.midPrint(node.rightNode)

    def lastPrint(self, node):
        if not node:
            return
        self.lastPrint(node.leftNode)
        self.lastPrint(node.rightNode)
        print(str(node.label))

    def findNode(self, node, value):
        if not node:
            return None
        if node.label == value:
            return node
        if node.label > value:
            return self.findNode(node.leftNode, value)
        else:
            return self.findNode(node.rightNode, value)

    def findPath(self, m, n):
        m_node = self.findNode(self.rootNode, m)
        n_node = self.findNode(self.rootNode, n)
        paths = []
        if n_node.level > m_node.level:
            tnode = n_node
            ln = m_node
            rn = None
            while tnode:
                paths.append(tnode.label)
                tnode = tnode.parent
                if tnode.level == m_node.level:
                    rn = tnode
                    break
            if paths[0] == m and paths[-1] == n:
                return paths
            paths.reverse()
            lPaths = []
            rPaths = []
            while ln is not None and rn is not None:
                if ln.label == rn.label:
                    lPaths.append(ln.label)
                    break
                lPaths.append(ln.label)
                rPaths.append(rn.label)
                ln = ln.parent
                rn = rn.parent
            rPaths.reverse()
            return lPaths + rPaths + paths

        if n_node.level < m_node.level:
            tnode = m_node
            ln = None
            rn = n_node
            while tnode:
                paths.append(tnode.label)
                tnode = tnode.parent
                if tnode.level == n_node.level:
                    ln = tnode
                    break
            if paths[0] == m and paths[-1] == n:
                return paths
            lPaths = []
            rPaths = []
            while ln is not None and rn is not None:
                if ln.label == rn.label:
                    lPaths.append(ln.label)
                    break
                lPaths.append(ln.label)
                rPaths.append(rn.label)
                ln = ln.parent
                rn = rn.parent
            rPaths.reverse()
            return paths + lPaths + rPaths
        if n_node.level == m_node.level:
            ln = m_node
            rn = n_node
            lPaths = []
            rPaths = []
            while ln is not None and rn is not None:
                if ln.label == rn.label:
                    lPaths.append(ln.label)
                    break
                lPaths.append(ln.label)
                rPaths.append(rn.label)
                ln = ln.parent
                rn = rn.parent
            rPaths.reverse()
            return lPaths + rPaths




s_list = input().split(' ')
bst = BST()
for s in s_list:
    bst.add(int(s))

m_n_list = input().split(' ')
m = int(m_n_list[0])
n = int(m_n_list[1])
paths = bst.findPath(m, n)
ms = map(lambda x: str(x), paths)
s = '->'.join(ms)
print(s)





