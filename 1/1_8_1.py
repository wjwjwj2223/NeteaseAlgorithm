from itertools import combinations


def transform(t):
    return list(t)

def take(elem):
    return elem[0]

if __name__ == '__main__':
    s = int(input())
    h = int(input())
    temp = list(range(1, s + 1))
    combination = list(combinations(temp, h))
    t1 = map(transform, combination)
    t2 = list(t1)
    for t in t2:
        t.sort(reverse=True)
    t2.sort(reverse=True)
    for t in t2:
        print(t)