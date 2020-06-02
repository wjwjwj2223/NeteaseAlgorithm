
import copy

class INode(object):
    """docstring for ClassName"""
    def __init__(self, item, n):
        self.item = item
        self.next = n

class INodeList(object):

    def __init__(self, item):
        self.firstNode = INode(item, None)
        self.lastNode = self.firstNode
        self.size = 1


    def addFirst(self, item):
        self.firstNode = INode(item, self.firstNode)
        self.size += 1

    def addLast(self, item):
        self.lastNode.next = INode(item, None)
        self.lastNode = self.lastNode.next
        self.size += 1

    def output(self):
        tempNode = self.firstNode
        s = str(tempNode.item)
        while tempNode.next:
            tempNode = tempNode.next
            s += "->"
            s += str(tempNode.item)
        return s

    def reverse(self, m, n):
        leftNode = None
        rightNode = None
        node = None
        if m == n:
            return
        if m == 0 and n == self.size - 1:
            self.reverseNodes(self.firstNode)
            return
        if m == 0:
            count = 0
            tempNode = self.firstNode
            node = self.firstNode
            while tempNode.next:
                if count == n:
                    rightNode = tempNode.next
                    tempNode.next = None
                    break
                count += 1
                tempNode = tempNode.next
            self.reverseNodes(node, leftNode, rightNode)
            self.firstNode = tempNode
            return
        if n == self.size - 1:
            count = 0
            tempNode = self.firstNode
            while tempNode:
                if count == m - 1:
                    leftNode = tempNode
                if count == m:
                    node = tempNode
                    break
                count += 1
                tempNode = tempNode.next
            self.reverseNodes(node, leftNode, rightNode)
            return
        count = 0
        tempNode = self.firstNode
        while tempNode.next:
            if count == m - 1:
                leftNode = tempNode
            if count == m:
                node = tempNode
            if count == n:
                rightNode = tempNode.next
                tempNode.next = None
                leftNode.next = None
                break
            count += 1
            tempNode = tempNode.next
        self.reverseNodes(node, leftNode, rightNode)


    def reverseNodes(self, node, leftNode, rightNode):
        pre = None
        cur = None
        last = None
        pre = node
        temp = node.next
        last = node.next.next
        while temp:
            last = temp.next
            cur = temp
            cur.next = pre
            pre = temp
            temp = last

        if leftNode:
            leftNode.next = pre
        node.next = rightNode


s = input()
last_item = input()
s_list = s.split(' ')
s_list = list(map(lambda a: int(a), s_list))
b_list = last_item.split(' ')

nodeList = INodeList(s_list[0])
for item in s_list[1:]:
	nodeList.addLast(item)

nodeList.reverse(int(b_list[0]), int(b_list[1]))
print(nodeList.output())

