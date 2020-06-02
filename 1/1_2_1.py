

class LinkedNode(object):
	def __init__(self, first, rest):
		super(LinkedNode, self).__init__()
		self.first = first
		self.restNode = rest

def formatPrint(node):
	print(node.first,  end = '')
	if node.restNode:
		print('->',  end = '')
		formatPrint(node.restNode)

inputs = input()
numbers = inputs.split(" ")
map(lambda a: int(a), numbers)
temp = None
firstNode = None
for idx, number in enumerate(numbers):
	if temp:
		temp.restNode = LinkedNode(number, None)
		temp = temp.restNode
	else:
		firstNode = LinkedNode(number, None)
		temp = firstNode

addNumber = input()
addInt = int(addNumber)

temp = firstNode
while temp.restNode:
	temp = temp.restNode
temp.restNode = LinkedNode(addInt, None)

formatPrint(firstNode)