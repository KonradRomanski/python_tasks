def ssplit(li):
    w = []
    t = ""
    f = False
    for i in enumerate(li):
        if i[1] == "=": f =True
        if (i[1] == "-" or i[1] == "+" or i[0] == len(li) - 1) and i[0] != 0 or i[1] == "=":
            if i[0] == len(li) - 1:
                t += i[1]
            if t != "":
                w.append(t)
                t = ""

            if (i[1] == "-" and f == False) or (i[1] == "+" and f == True) or (i[1] == "=" and li[i[0]+1] != "-"):
                t = "-" + t

        else:
            t += i[1]
    return w


def equation(li):
    f = 1
    a, b = 0, 0
    li = ssplit(li)
    # print(li)
    for i in li:
        # print("~~", i[:-1], a, b)
        if i == "x":
            a += 1
        elif i == "-x":
            a += -1
        elif i[-1:] == "x":
            a += int(i[:-1])
        else:
            b += int(i)
    # print("##", a, b)
    if a ==0: return "NO"
    else: return b/a*(-1)

def main():
    # print(ssplit("-4r-h6-d3+4f=-6+9-g5+6"))
    z = int(input())
    for i in range(z):
        ll = input()
        print(equation(ll))


main()
