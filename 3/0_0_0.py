
class QuickFindDS(object):

    def __init__(self, N):
        self.__id = list(range(0, N))
        print(self.__id)

    def isConnect(self, p, q):
        pid = self.__id[p]
        qid = self.__id[q]
        return pid == qid

    def connect(self, p, q):
        pid = self.__id[p]
        qid = self.__id[q]
        self.__id = [qid if x == pid else x for x in self.__id]