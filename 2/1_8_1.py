n = input()
result = []
methods = 0
if not int(n):
    print(0)
    exit()
for i in range(0, int(n)):
    line = input()
    line_list = line.split(' ')
    line_i = [int(float(j)) for j in line_list]
    if len(line_i) != int(n):
        exit()
    result.append(line_i)


def breakthrough(n, result):

    def go(line, row):
        if line >= n or row >= n:
            return
        if line == n - 1 and row == n - 1:
            global methods
            methods += 1
            return
        if result[line][row] == 1:
            return
        go(line + 1, row)
        go(line, row + 1)

    go(0, 0)


breakthrough(int(n), result)
print(methods)
