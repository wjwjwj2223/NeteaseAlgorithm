
def sortList(s_list, li, ri):
    if li >= ri:
        return
    store_index = li + 1
    for i in range(li + 1, ri + 1):
        if s_list[i] < s_list[li]:
            s_list[i], s_list[store_index] = s_list[store_index], s_list[i]
            store_index += 1
    s_list[li], s_list[store_index - 1] = s_list[store_index - 1], s_list[li]
    sortList(s_list, li, store_index - 1)
    sortList(s_list, store_index, ri)


s_list = input().split(' ')
s_set = set()
for s in s_list:
    items = s.split(':')
    for x in range(int(items[0]), int(items[1]) + 1):
        s_set.add(x)
t_list = list(s_set)
sortList(t_list, 0, len(t_list) - 1)

index = None
start = t_list[0]
end = t_list[len(t_list) - 1]

for t in t_list:
    if t == start:
        start = t
        index = t
    if index != t:
        print(str(start) + ':' + str(index - 1))
        start = t
        index = t
    if t == end:
        if start == end:
            print(start)
            break
        print(str(start) + ':' + str(t))
        break
    index += 1