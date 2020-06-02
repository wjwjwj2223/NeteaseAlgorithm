import copy


def combine(lst, l):
    result = []
    tmp = [0] * l
    length = len(lst)

    def next_num(li=0, ni=0):
        if ni == l:
            result.append(copy.copy(tmp))
            return
        for lj in range(li, length):
            tmp[ni] = lst[lj]
            next_num(lj + 1, ni + 1)

    next_num()
    return result
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    for item in combine([i for i in range(n, 0, -1)], m):
        print(item)