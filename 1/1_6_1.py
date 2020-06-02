

def check(list):
    man_list = []
    for item in list:
        if item == 'f':
            man_list.append(item)
        elif item == 'm':
            if len(man_list) == 0:
                return False
            man_list.pop()
        else:
            return False
    if len(man_list) == 0:
        return True
    return False

if __name__ == '__main__':
    s = input()
    s_list = list(s)
    s_list.reverse()
    print(check(s_list))