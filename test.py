def main():
    Students = {}
    Tests = {}
    N = int(input())
    for i in range(N):
        li = input().split()
        if  not li[0] in Students: Students[li[0]] = [0, 0]

        for j in li[1:]:
            newli = j.split(":")
            if not newli[0] in Tests: Tests[newli[0]] = [0, 0]
            Tests[newli[0]][0] += 1
            Tests[newli[0]][1] += float(newli[1])

            Students[li[0]][0] += 1
            Students[li[0]][1] += float(newli[1])

    for i in Students.items():
        Students[i[0]] = Students[i[0]][1]/Students[i[0]][0]
    for i in Tests.items():
        Tests[i[0]] = Tests[i[0]][1]/Tests[i[0]][0]

    # for i in Students.items(): print(i)
    # for i in Tests.items(): print(i)

    A = []
    B = []
    for i in Students.items():
        A.append(i[0])
    A.sort()
    for i in Tests.items():
        B.append(i[0])
    B.sort()

    for i in A:
        print(i, Students[i])

    for i in B:
        print(i, Tests[i])
    # print(A)
    # print(B)


main()


# 4
# jan a:4 b:3
# artur d:2 a:7
# karol c:3.5 a:4 d:4 b:5
# sylwester eee:4

# def main():
#     Z = {}
#     lis = []
#     N = int(input())
#     for i in range(N):
#         li = input().split()
#         Z.append([li[0]])
#
#         x = 0
#         s = 0
#
#         for j in li[1:]:
#             x += 1
#             a = j.split(":")
#             print(a)
#             s += int(a[1])
#
#         a[0]
#         Z[i].append(s/x)
#         print(Z)
#
#
# main()

# main()

# class Student():
#     def __init__(self, name, sr):
#         name.self = name
#         sr.self=sr

# def main()
#     lis = []
#     N = int(input())
#     for i in range(N):
#         li = input().split()

#         temp = Student(li[0], )


# main()