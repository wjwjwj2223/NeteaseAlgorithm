from functools import reduce

s_list = input().split(' ')
s_dict = dict()


for item in s_list:
    item_list = list(item)
    item_list.sort()
    sortedItem = ''.join(item_list)
    if sortedItem not in s_dict:
        s_dict[sortedItem] = 1
    else:
        s_dict[sortedItem] = s_dict[sortedItem] + 1

count = 0
for s in s_dict:
    if s_dict[s] > 1:
        count += 1
print(count)