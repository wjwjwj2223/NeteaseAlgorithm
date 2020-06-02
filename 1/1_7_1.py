

def check(mainlist):
    man_list = []
    for item in mainlist:
        if item.startswith('f'):
            man_list.append(item)
        elif item.startswith('m'):
            if len(man_list) == 0:
                return False
            lastMan = man_list[len(man_list) - 1]
            if list(item)[1] == list(lastMan)[1]:
                man_list.pop()
            else:
                return False
        else:
            return False
    if len(man_list) == 0:
        return True
    return False

if __name__ == '__main__':
    s = input()
    s_list = s.split(' ')
    s_list.reverse()
    print(check(s_list))