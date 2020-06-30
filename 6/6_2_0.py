
s_list = input().split(' ')

count = 0

for i in range(0, len(s_list)):
    for j in range(i + 1, len(s_list)):
        if s_list[j] < s_list[i]:
            count += 1

print(count)