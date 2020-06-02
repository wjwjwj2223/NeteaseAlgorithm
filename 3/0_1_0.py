
class QuickUnionDS(object):

    # 0 1 2 3 4 5 6 7 8
    # 0 1 2 3 4 5 6 7 8
    def __init__(self, N):
        self.__id = list(range(0, N))
        print(self.__id)

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
        def findRoot(i):
            id = self.__id[i]
            if id == i:
                return id
            else:
                return findRoot(id)

        p_root_id = findRoot(p)
        q_root_id = findRoot(q)
        self.__id[p_root_id] = q_root_id
