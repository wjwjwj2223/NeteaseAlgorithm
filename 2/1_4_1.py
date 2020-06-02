import math

stack = []


def permutation(n, from_num):
    global stack
    if n == from_num:
        stack.append(str(n))
        output()
        stack.pop()
    if from_num == 1:
        output()
    else:
        sqrt_n = int(math.sqrt(n))
        if from_num > 2:
            start_num = from_num
        else:
            start_num = 2
        for i in range(start_num, sqrt_n + 1):
            if n % i == 0:
                stack.append(str(i))
                permutation(int(n / i), i)
                stack.pop()
        stack.append(str(n))
        output()
        stack.pop()

def output():
    s = '{}='.format(n)
    s += '*'.join(stack)
    print(s)

n = int(input())
permutation(n, 2)
