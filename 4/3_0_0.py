
class LinkedNode(object):
    def __init__(self, value, hashCode, next=None):
        self.label = value
        self.next = next
        self.hashCode = hashCode


class LinkedList(object):

    def __init__(self):
        self.firstNode = None
        self.lastNode = None

    def addNode(self, value, hashCode):
        if not self.firstNode:
            self.firstNode = LinkedNode(value, hashCode= hashCode)
            self.lastNode = self.firstNode
        else:
            self.lastNode.next = LinkedNode(value, hashCode= hashCode)
            self.lastNode = self.lastNode.next

    def conatinsNode(self, hashCode):
        node = self.firstNode
        if not node:
            return False
        while node:
            if node.hashCode == hashCode:
                return True
            node = node.next
        return False


class HashTable(object):

    def __init__(self):
        self.size = 32
        self.count = 0
        self.l_list = [LinkedList() for _ in range(0, self.size)]

    def addValue(self, value):
        hashValue = hash(value)
        index = hashValue % self.size
        linkedList = self.l_list[index]
        contains = linkedList.conatinsNode(hashValue)
        if contains:
            return
        linkedList.addNode(value, hashValue)
        self.l_list[index] = linkedList
        self.count += 1
        if self.count / len(self.l_list) > 1.5:
            self.resize()

    def resize(self):
        self.size = self.size * 2
        new_list = [LinkedList() for _ in range(0, self.size)]
        for linkedList in self.l_list:
            node = linkedList.firstNode
            while node:
                hashCode = node.hashCode
                index = hashCode % self.size
                new_linked_list = new_list[index]
                new_linked_list.addNode(node.label, hashCode)
                node = node.next
        self.l_list = new_list

    def contains(self, value):
        hashValue = hash(value)
        index = hashValue % self.size
        linkedList = self.l_list[index]
        return linkedList.conatinsNode(hashValue)


n = int(input())
hashTable = HashTable()
for i in range(0, n):
    v = input()
    hashTable.addValue(v)
m = int(input())
for i in range(0, m):
    t = input()
    print(hashTable.contains(t))


