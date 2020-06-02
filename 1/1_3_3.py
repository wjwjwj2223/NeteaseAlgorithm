

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

        if m == n:
            return

        leftNode = None
        rightNode = None

        pre = None
        cur = None
        later = None

        pre = None
        temp = self.firstNode
        later = self.firstNode.next

        innerLeftNode = None
        innerRightNode = None

        count = 0
        while temp:
            if count < m - 1 and temp:
                count += 1
                temp = temp.next
            if count == m - 1 and temp:
                leftNode = temp
                pre = temp
                temp = temp.next
                count += 1
            if count == m and temp:
                innerLeftNode = temp
                pre = temp
                temp = temp.next
                count += 1
            if count > m and count <= n and temp:
                if count == n:
                    innerRightNode = temp
                    if m == 0:
                        self.firstNode = innerRightNode
                later = temp.next
                cur = temp
                cur.next = pre
                pre = temp
                temp = later
                count += 1
            if count == n + 1 and temp:
                rightNode = temp
                pre = temp
                temp = temp.next
                count += 1
            if count > n:
                break


        if leftNode:
            leftNode.next = innerRightNode
        innerLeftNode.next = rightNode
        


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

