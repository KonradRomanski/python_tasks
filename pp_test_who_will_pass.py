def main():
    a = int(input())
    M = [[0 for i in range(a)] for j in range(a)]
    W = [[0 for i in range(a)] for j in range(a)]
    for i in range(a):
        l = [int(i) for i in input().split()]
        for j in range(a):
            M[i][j] = l[j]
            W[i][j] = l[j]

    # M[0][0] = a
    # print(M, W, sep='\n')

    M.insert(0, [3 for i in range(a+2)])
    for i in range(a+1):
        M[i] = [3] + M[i] + [3]
    M.insert(a+1, [3 for i in range(a+2)])

    # print(M, W, sep="\n")

    for i  in range(a):
        for j in range(a):
            if M[i+1][j+1] >= 3:
                W[i][j] = 1
            else:
                y = i + 1
                x = j + 1
                S = M[y+1][x] + M[y+1][x+1] + M[y+1][x-1] + M[y-1][x] + M[y-1][x+1] + M[y-1][x-1] + M[y][x-1] + M[y][x+1]
                sr = S/8
                if sr >= 3:
                    W[i][j] = 1
                else:
                    W[i][j] = 0
    # print(M, W, sep="\n")
    for i in range(a):
        for j in range(a):
            print(W[i][j], end=" ")
        print()
main()
