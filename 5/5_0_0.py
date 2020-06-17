class MinHeap(object):

    def __init__(self):
        self.__datas = [None]
        self.__size = 0

    def add(self, value):
        self.__datas.append(value)
        self.__size += 1
        self.shitUp(self.__size)

    def get_smallest(self):
        return self.__datas[1]

    def extractMin(self):
        self.__datas[1] = self.__datas.pop()
        self.__size -= 1
        self.shitDown()

    def getSize(self):
        return self.__size

    def shitUp(self, index):
        if index == 1:
            return
        parent_index = index // 2
        if self.__datas[parent_index] > self.__datas[index]:
            self.__swap(index, parent_index)
            self.shitUp(parent_index)


    def shitDown(self):
        if self.__size <= 2:
            return
        currentIndex = 1
        michal = self.minChild(currentIndex)
        while michal and self.__datas[currentIndex] > self.__datas[michal]:
            self.__swap(currentIndex, michal)
            currentIndex = michal
            michal = self.minChild(currentIndex)

    def size(self):
        return len(self.__datas)

    def isEmpty(self):
        return len(self.__datas) == 0

    def leftChild(self, index):
        return index * 2

    def rightChild(self, index):
        return index * 2 + 1

    def minChild(self, index):
        li = self.leftChild(index)
        ri = self.rightChild(index)
        mini = None
        if ri <= self.__size:
            if self.__datas[li] > self.__datas[ri]:
                mini = ri
            else:
                mini = li
        elif li <= self.__size:
            mini = li
        return mini

    def __swap(self, a, b):
        self.__datas[a], self.__datas[b] = self.__datas[b], self.__datas[a]


source = input()
s_list = source.split(' ')
heap = MinHeap()
for s in s_list:
    heap.add(int(s))

m = int(input())
for i in range(0, m):
    heap.extractMin()
print(heap.get_smallest())