def res(li):
    w = 0.0
    for i in li:
        w += 1/i
    w = 1/w
    return w


N = int(input())
l = list(map(int, input().split()))
print(res(l))
