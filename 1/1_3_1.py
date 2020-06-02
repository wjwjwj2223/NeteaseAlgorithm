
inputs = input()
numbers = inputs.split(" ")
map(lambda a: int(a), numbers)


inputs = input()
boundarys = inputs.split(" ")
map(lambda a: int(a), boundarys)

leftBoundary = int(boundarys[0])
rightBoundary = int(boundarys[1])
rightBoundary = rightBoundary + 1
boundaryNumbers = numbers[leftBoundary: rightBoundary]
boundaryNumbers.reverse()
leftNumbers = numbers[0: leftBoundary]
rightNumbers = numbers[rightBoundary: ]

numbers = leftNumbers + boundaryNumbers + rightNumbers
formatString = '->'.join(numbers)
print(formatString)