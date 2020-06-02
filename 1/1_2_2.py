
class LinkedNode(object):
	def __init__(self, first, rest):
		super(LinkedNode, self).__init__()
		self.first = first
		self.restNode = rest


# def formatPrint(node):
# 	print(node.first,  end = '')
# 	if node.restNode:
# 		print('->',  end = '')
# 		formatPrint(node.restNode)


inputs = input()
numbers = inputs.split(" ")
map(lambda a: int(a), numbers)


firstNode = None
lastNode = None
temp = None
formatString = None
for idx, number in enumerate(numbers):
	if temp:
		temp.restNode = LinkedNode(number, None)
		temp = temp.restNode
		lastNode = temp
		formatString += "->"
		formatString += str(temp.first)
	else:
		firstNode = LinkedNode(number, None)
		temp = firstNode
		formatString = temp.first

addNumber = input()
addInt = int(addNumber)
lastNode.restNode = LinkedNode(addInt, None)
lastNode =  lastNode.restNode
formatString += "->"
formatString += str(lastNode.first)

print(formatString)

