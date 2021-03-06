
class WeightQuickUnionWithPathCompressionDS(object):

    # 0 1 2 3 4 5 6 7 8
    # 0 1 2 3 4 5 6 7 8
    def __init__(self, N):
        self.__id = list(range(0, N))
        self.__count = [1] * N
        self.__root_count = N

    def getRootCount(self):
        return self.__root_count

    def isConnect(self, p, q):
        def findRoot(i):
            id = self.__id[i]
            if id == i:
                return id
            else:
                return findRoot(id)
        p_root_id = findRoot(p)
        q_root_id = findRoot(q)
        return p_root_id == q_root_id

    def connect(self, p, q):
        paths = []
        def findRoot(i):
            id = self.__id[i]
            if id == i:
                for path in paths:
                    self.__id[path] = id
                paths.clear()
                return id
            else:
                paths.append(id)
                return findRoot(id)
        p_root_id = findRoot(p)
        q_root_id = findRoot(q)
        p_root_count = self.__count[p_root_id]
        q_root_count = self.__count[q_root_id]
        if p_root_id == q_root_id:
            return
        if p_root_count > q_root_count:
            self.__id[q_root_id] = p_root_id
            self.__count[p_root_id] = self.__count[p_root_id] + self.__count[q_root_id]
        else:
            self.__id[p_root_id] = q_root_id
            self.__count[q_root_id] = self.__count[q_root_id] + self.__count[p_root_id]
        self.__root_count -= 1

N = int(input())
quickDS = WeightQuickUnionWithPathCompressionDS(N)
n = int(input())
for _ in range(n):
    item = input()
    items = item.split(' ')
    quickDS.connect(int(items[0]), int(items[1]))

print(quickDS.getRootCount())