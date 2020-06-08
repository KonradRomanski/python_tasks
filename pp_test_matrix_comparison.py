# def mmm(matrix_2, c1, c2, matrix_1, matrix_2_rows, matrix_2_columns):
#     matrix_to_compare = []
#     for i in range(matrix_2_rows):
#         t = []
#         for j in range(matrix_2_columns):
#             if i != c1 and j != c2:
#                 t.append(matrix_2[i][j])
#         if i != c1:
#             matrix_to_compare.append(t)
#     print(matrix_to_compare)
#     if matrix_1 == matrix_to_compare: return True
#     return False
#
#
# def main():
#     matrix_1_rows, matrix_1_columns = list(map(int, input().split()))
#     matrix_1 = []
#     for i in range(matrix_1_rows):
#         a = input().split()
#         matrix_1.append(a)
#     matrix_2_rows, matrix_2_columns = list(map(int, input().split()))
#     matrix_2 = []
#     for i in range(matrix_2_rows):
#         a = input().split()
#         matrix_2.append(a)
#     print(matrix_1, matrix_2)
#
#     for i in range(matrix_2_rows):
#         for j in range(matrix_2_columns):
#             if mmm(matrix_2, i, j, matrix_1, matrix_2_rows, matrix_2_columns):
#                 print(True)
#                 return
#     print(False)
#     return
#
#
# main()
#
# # 3 3
# # a b c
# # d e f
# # g h i
# # 4 4
# # a b c t
# # t t t t
# # d e f t
# # g h i t


def mmm(matrix_2, c1, c2, matrix_1, matrix_2_rows, matrix_2_columns):
    matrix_to_compare = []
    for i in range(matrix_2_rows):
        t = []
        for j in range(matrix_2_columns):
            if i != c1 and j != c2:
                t.append(matrix_2[i][j])
        if i != c1:
            matrix_to_compare.append(t)
    print(matrix_to_compare)
    if matrix_1 == matrix_to_compare: return True
    return False


def main():

    matrix_2_rows = int(input())
    matrix_2_columns = matrix_2_rows
    matrix_1_rows = matrix_2_rows-1
    matrix_1_columns = matrix_1_rows
    matrix_1 = []
    matrix_2 = []

    for i in range(matrix_2_rows):
        a = input().split()
        matrix_2.append(a)
    print(matrix_1, matrix_2)

    for i in range(matrix_1_rows):
        a = input().split()
        matrix_1.append(a)


    for i in range(matrix_2_rows):
        for j in range(matrix_2_columns):
            if mmm(matrix_2, i, j, matrix_1, matrix_2_rows, matrix_2_columns):
                print(True)
                return
    print(False)
    return


main()

# 3 3
# a b c
# d e f
# g h i
# 4 4
# a b c t
# t t t t
# d e f t
# g h i t