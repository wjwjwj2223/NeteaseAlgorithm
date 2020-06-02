

stack = []

def share(a_list):

    sumc = sum(a_list)
    averages = int(sumc / 2)

    def consume(index, target):
        if not target:
            return True
        elif index == 0:
            return a_list[index] == target
        else:
            return consume(index - 1, target - a_list[index]) or consume(index - 1, target)

    for target in range(averages, 0, -1):
        if consume(len(a_list) - 1, target):
            return sumc - target - target


n = input()
n_list = n.split(' ')
count = share([int(i) for i in n_list])
print(count)