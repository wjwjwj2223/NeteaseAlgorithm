
s_list = input().split(' ')

s_set = set()
for s in s_list:
    sortList = list(s)
    sortList.sort()
    s_set.add(''.join(sortList))

result = list(s_set)
result.sort()
for r in result:
    print(r, end=' ')