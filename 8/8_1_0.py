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

        def containsNode(node, w):
            if not node:
                return False
            if not w:
                return node.isWord
            if w[0] == '*':
                for n in node.next:
                    if containsNode(node.next.get(n), w[1:]):
                        return True
            return containsNode(node.next.get(w[0]), w[1:])

        return containsNode(self.root, word)


s_list = input().split(' ')
trie = Trie()
for s in s_list:
    trie.addWord(s)

words = input().split(' ')
results = []

for w in words:
    results.append(trie.contains(w))

for r in results:
    print(r, end=' ')
