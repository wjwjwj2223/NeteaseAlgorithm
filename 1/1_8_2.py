
stack = []

# [1,2,3,4,5]
# arr = [5,4,3,2,1]
# index = 4
# count = 2

def permutation(arr, index, count):
    global stack
    if count == 1:
        for i in range(index, len(arr)):
            stack.append(arr[i])
            print(stack)
            stack.pop()
    elif index < len(arr):
        stack.append(arr[index])
        permutation(arr, index + 1, count - 1)
        stack.pop()
        permutation(arr, index + 1, count)

n = int(input())
m = int(input())
permutation([i for i in range(n, 0, -1)], 0, m)