def squares(x, y):
    x = int(x)
    y = int(y)
    w = 0
    for i in range(x, y+1):
        w += i*i
    return w


def main():
    l = input()
    l = l.split()
    print(squares(l[0], l[1]))


main()
