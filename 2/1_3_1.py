import math


def p(M):
    return r(0, M)

def p1(n):
    for i in range(n):
        for j in range(0, n, 2):
            print('Hi!')

def p2(n):
    for i in range(n):
        j = 1
        while j<n:
            print('Hi!')
            j = j*2

def r(i, M):
    if i >= M:
        return 0
    if s(i) > 0:
        return i
    return r(i + 1, M)

def s(k):
    if k <= 0:
        return 0
    if h(k):
        return k
    return s(k - 1)

count = 0
def p3(n):
    global count
    count += 1
    if n<=1:
        return
    p3(n/2)
    p3(n/2)



def h(k):
    return k

def p4(n):
    m = int(((15 + math.ceil(3.2 / 2)) * (math.floor(10 / 5.5) / 2.5) * math.pow(2, 5)))
    for i in range(m):
        print("Hi")

def p5(n):
    i = 1
    while i<n*n:
        for j in range(i):
            print("Hi")
        i *= 2

p3(10000000)
print(count)