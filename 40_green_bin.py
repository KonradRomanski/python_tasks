def silnia(n):
    w = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            w *= i
    return w


def newton(x, y):
    if x < y or x < 0 or y < 0 :
        return 0
    else:
        return int(silnia(x)/(silnia(y) * silnia(x-y)))


def main():
    Z = {}
    N = int(input())
    for i in range(N):
        li = input()
        li = ''.join(sorted(li))
        # print(li)
        if not li in Z: Z[li] = 0
        Z[li] += 1
    # print(Z)
    w = 0
    for i in Z.items():
        Z[i[0]] = newton(Z[i[0]], 2)
        w += Z[i[0]]
        # w += newton(Z[i[0]], 2)
        # print("$$$", Z[i[0]])
        # print(Z[i[0]])
    print(w)
main()

# 5
# abaaaaaaaa
# oneplustwo
# aaaaaaaaba
# twoplusone
# aaaabaaaaa