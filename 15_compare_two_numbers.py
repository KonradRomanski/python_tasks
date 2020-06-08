def compare(x, y):
    w = ""
    if x == y:
        w = ("n is equal m:  " + str(x))
    elif x > y:
        w = (str(x) + "  is greater than  " + str(y))
    elif x < y:
        w = (str(x) + "  is smaller than  " + str(y))

    return w


t = int(input())
n = []
for i in range(t):
    d = input()
    d = d.split()
    n.append(d[0])
    n.append(d[1])
g = 0
for j in range(t):
    print(compare(int(n[g]), int(n[g+1])))
    g += 2
# 2
# 3 5
# 8 9