def bije(l, sz):
    x = l[0]
    y = l[1]
    # print(x, y, type(x))
    sz[x] = sz[x][:y] + "#" + sz[x][y + 1:]
    if sz[l[0]].find("|") != -1: return True #poziom
    a = 1
    for i in sz:
        if i[l[1]] == "|": return True #pion

    for i in range(len(sz)):
        for j in range(len(sz[i])):
            if abs(i - x) == abs(j - y) and sz[i][j] == "|": return True #ukosy
    return False



def hetman(sz):
    figury = []
    for i in range(len(sz)):
        aa = sz[i]
        f = sz[i].find("$")

        while f >= 0:

            figury.append((i, f))
            # print(sz[i], f, len(sz[i]))
            # if f == len(sz[i])-1:
            #     sz[i] = sz[i][:f] + "|"
            # else:
            # print(sz[i])
            sz[i] = sz[i][:f] + "|" + sz[i][f+1:]
            # print(sz[i])
            f = sz[i].find("$")
        # sz[i] = aa

    # print(sz)
    # print(figury)

    for i in figury:
        if bije(i, sz):
            return True
    return False



def main():
    A = 0
    T = int(input())
    P = []
    for i in range(T):
        N = int(input())

        for j in range(N):
            li = input()
            P.append(li)
        if hetman(P):
            print("TAK")
        else:
            print("NIE")
        P = []


main()