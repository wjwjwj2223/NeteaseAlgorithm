
import math

m = int(((15 + math.ceil(3.2 / 2)) * (math.floor(10 / 5.5) / 2.5) * math.pow(2, 5)))


print(m)

def p5(n):
    i = 1
    while i<n*n:
        for j in range(i):
            print("Hi")
        i *= 2

print(p5(4))