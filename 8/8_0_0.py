class Node(object):
    def __init__(self, isWord):
        self.isWord = isWord
        self.next = dict()


class Trie(object):
    def __init__(self):
        self.root = Node(False)
        self.size = 0

    def getSize(self):
        return self.size

    # 添加单词
    def addWord(self, word):
        cur = self.root
        for c in list(word):
            if not cur.next.get(c):
                cur.next[c] = Node(False)
            cur = cur.next.get(c)

        if not cur.isWord:
            cur.isWord = True
            self.size += 1

    # 查询单词work是否在trie中
    def contains(self, word):
        cur = self.root
        for c in list(word):
            if not cur.next.get(c):
                return False
            cur = cur.next.get(c)
        return cur.isWord

    def accum(self, curNode, prefix, res):
        for key in curNode.next:
            if curNode.next[key].isWord:
                res.append(prefix + key)
            self.accum(curNode.next[key], prefix + key, res)

    def findWords(self, prefixWord):
        cur = self.root
        results = []
        for c in list(prefixWord):
            if not cur.next.get(c):
                return []
            cur = cur.next.get(c)
        if cur.isWord:
            results.append(prefixWord)
        self.accum(cur, prefixWord, results)
        return results


s_list = input().split(' ')
trie = Trie()
for s in s_list:
    trie.addWord(s)

prefix = input()
results = trie.findWords(prefix)
results.sort()
for x in results:
    print(x, end=' ')