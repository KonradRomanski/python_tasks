def msum(c):
    ma = 0
    w = 0
    for i in c:
        w += i
        if w < 0:
            w = 0
        elif ma < w:
            ma = w
    return ma


def fms(M, n):
    ma = 0
    for l in range(n):
        t = [0] * n
        for r in range(l, n):
            for i in range(n):
                t[i] += M[i][r]
            tsum = msum(t)
            if tsum > ma:
                ma = tsum
    return ma


n = int(input())
mat = []
for i in range(n):
    li = list(map(int, input().split()))
    mat.append(li)

print(fms(mat, n))
