# W = []
# M = []
#
# def zerowanko(x, y, a, b):
#     # print(W)
#     for i in range(y):
#         for j in range(x):
#             if j == a or i == b:
#                 # print(M, W)
#                 W[j][i] = 0
#                 # print(M, W)
#     return A
#
#
# def main():
#
#     d = list(map(int, input().split()))
#     x = d[0]
#     y = d[1]
#
#     for i in range(y):
#         u = list(map(int, input().split()))
#         M.append(tuple(u))
#         W.append(u)
#     # print(M)
#     # print(W)
#     for i in range(y):
#         for j in range(x):
#             if M[j][i] == 0:
#                 print(x, y, j, i)
#                 print(W, M)
#                 print("ss")
#                 W = zerowanko(x, y, j, i)
#
#     for i in range(y):
#         for j in range(x):
#             print(W[i][j], sep="", end=" ")
#         print()
#
#
# main()
#
# # # M = []
# # # W = []
# #
# #
# # # def main():
# # #     d = list(map(int, input().split()))
# # #     x = d[0]
# # #     y = d[1]
# # #
# # #     for i in range(y):
# # #         u = list(map(int, input().split()))
# # #         M.append(u)
# # #         W.append(u)
# # #     # print(M)
# # #     # print(W)
# # #     for i in range(y):
# # #         for j in range(x):
# # #             if W[j][i] == 0:
# # #                 # print(x, y, j, i)
# # #                 # print(W, M)
# # #                 for r in range(y):
# # #                     for s in range(x):
# # #                         if s == j or r == i:
# # #                             W[r][s] = 0
# # #
# # #     for i in range(y):
# # #         for j in range(x):
# # #             print(W[i][j], sep="", end=" ")
# # #         print()
# # #
# # #
# # main()

# def main():
#     fl = list(map(int, input().split()))
#     y = fl[0]
#     x = fl[1]
#
#     M = []
#     W = []
#
#     for i in range(y):
#         fl = list(map(int, input().split()))
#         M.append(tuple(fl))
#         W.append(list(fl))
#     print(M, W)
#
#     for i in range(y):
#         for j in range(x):
#
#             if M[i][j] == 0:
#
#                 for u in range(y):
#                     for v in range(x):
#
#                         if i == u or j == v:
#                             W[u][v] = 0
#     print(M, W)
#
#     for i in range(y):
#         for j in range(x):
#             print(W[i][j], end = ' ')
#         print()
#
# main()


def main():
    y, x = list(map(int, input().split()))

    M = []
    W = []

    for i in range(y):
        pk = list(map(int, input().split()))
        M.append(tuple(pk))
        W.append(list(pk))

    print(M, W)

    for i in range(y):
        for j in range(x):

            if M[i][j] == 0:

                for u in range(y):
                    for v in range(x):

                        if i == u or j == v:
                            W[u][v] = 0
    print(M, W)

    for i in range(y):
        for j in range(x):
            print(W[i][j], end = ' ')
        print()

main()