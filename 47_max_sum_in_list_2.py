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


li = list(map(int, input().split()))
print(msum(li))
