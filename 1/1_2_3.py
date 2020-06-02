
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
		
		
s = input()
last_item = input()
s_list = s.split(' ')


nodeList = INodeList(s_list[0])
for item in s_list[1:]:
	nodeList.addLast(item)
nodeList.addLast(last_item)
print(nodeList.output())

