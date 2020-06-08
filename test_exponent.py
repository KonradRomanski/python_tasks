def sil(a):
    if a == 0 or a == 1:
        return 1
    else:
        return sil(a-1)*a


def exponent(p, d):
    W = 0
    l = 1
    a = 0
    while abs(W - l) >= d :
        l = W
        W += (p**a) / (sil(a))
        a += 1
    return W


def main():
    # print(sil(4))
    li = input().split()
    x = int(li[0])
    E = float(li[1])
    print("%.50f %.2f" % (exponent(x, E), exponent(x, E)))

main()