def proper(st):
    if len(st) == 1 or len(st) % 2 != 0:
        return False
    bbb = {"(", "[", "{"}
    sta = []
    for i in st:
        # print(sta, i)
        if i in bbb:
            sta.append(i)
        else:
            g = sta.pop()
            print(sta, g, i)
            if not ((g in bbb) and ((g == "{" and i == "}")
                         or (g == "(" and i == ")")
                         or (g == "[" and i == "]"))):
                return False
    return True

# WRONG
# def proper2(st):
#     if len(st) == 1 or len(st) % 2 != 0: return False
#     for i in range(1, len(st) - 1):
#         if  (st[i - 1] == "{" and st[i] == "]") or (st[i-1] == "{" and st[i] == ")") or (st[i-1] == "[" and st[i] == ")")\
#                 or (st[i - 1] == "[" and st[i] == "}") or (st[i-1] == "(" and st[i] == "]") or (st[i-1] == "(" and st[i] == "}"):
#             print(st[i - 1], st[i])
#             return False
#     return True

    # def proper(st):
    # bbb = {"(", "[", "{"}
    # sta = []
    # for i in enumerate(st):
    #     print(sta)
    #     if i[1] in bbb:
    #         sta.append(i[1])
    #     else:
    #         if sta[i[0] - 1] in bbb \
    #                 and ((sta[i[0] - 1] == "{" and i[1] == "}") \
    #                      or (sta[i[0] - 1] == "(" and i[1] == ")") \
    #                      or (sta[i[0] - 1] == "[" and i[1] == "]")):
    #             sta.pop()
    #         else:
    #             return False
    # return True


def main():
    s = input()
    # proper(s)
    print(proper2(s))


main()
