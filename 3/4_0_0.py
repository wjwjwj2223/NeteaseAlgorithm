# 0 1 2 3 4 5 6 7 8 9
# 0 9 5 3
# 1 8

class SetDS(object):

    def __init__(self):
        self.__setList = []

    def getList(self):
        return self.__setList

    def isConnect(self, p, q):
        set1 = None
        set2 = None
        for setItem in self.__setList:
            if p in setItem:
                set1 = setItem
            if q in setItem:
                set2 = setItem
        if set1 and set2 and set1 == set2:
            return True
        return False

    def connect(self, p, q):
        set1 = None
        set2 = None
        for setItem in self.__setList:
            if p in setItem:
                set1 = setItem
            if q in setItem:
                set2 = setItem
        if set1 and set2 and set1 == set2:
            return
        if set1 and set2 and set1 != set2:
            self.__setList.remove(set2)
            self.__setList.remove(set1)
            set1 = set1.union(set2)
            self.__setList.append(set1)
        if not set1 and not set2:
            self.__setList.append({p, q})
        if set1 and not set2:
            set1.add(q)
        if set2 and not set1:
            set2.add(p)

quickDS = SetDS()
N = int(input())
n = int(input())
for _ in range(n):
    item = input()
    items = item.split(' ')
    quickDS.connect(int(items[0]), int(items[1]))

setLists = quickDS.getList()
for setItem in setLists:
    N = N - len(setItem) + 1
print(N)