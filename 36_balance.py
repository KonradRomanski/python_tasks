def sum(ll):
    w = 0
    for i in ll:
        w+=i
    return w


def balance(ll):
    a = 0
    b = sum(ll)
    m = 99999999999999999999999999999999999999999999999
    for i in range(len(ll)):
        a += ll[i]
        b -= ll[i]
        g = abs(a - b)
        if g <  m: m = g
    return m

def main():
    a = input()
    li = list(map(int, input().split()))
    print(balance(li))


main()