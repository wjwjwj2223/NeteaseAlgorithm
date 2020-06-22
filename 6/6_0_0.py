class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __lt__(self, sdt):
        if self.score == sdt.score:
            if self.name == sdt.name:
                return self.age < sdt.age
            else:
                return self.name < sdt.name
        else:
            return self.score < sdt.score

    def __str__(self):
        return '{} {} {}'.format(self.name, self.age, self.score)


def sortStudent(s_list, li, ri):
    if li >= ri:
        return
    store_index = li + 1
    for i in range(li + 1, ri + 1):
        if s_list[i] < s_list[li]:
            s_list[i], s_list[store_index] = s_list[store_index], s_list[i]
            store_index += 1
    s_list[li], s_list[store_index - 1] = s_list[store_index - 1], s_list[li]
    sortStudent(s_list, li, store_index - 1)
    sortStudent(s_list, store_index, ri)


m = int(input())
students = []
for i in range(m):
    s = input().split(' ')
    students.append(Student(s[0], int(s[1]), int(s[2])))
sortStudent(students, 0, len(students) - 1)
for stu in students:
    print(stu)

