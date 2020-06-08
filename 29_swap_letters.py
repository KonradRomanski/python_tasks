fl = input().split()
n = int(fl[0])
m = int(fl[1])
li = input().split()
for i in range(m):
    z = input().split()
    z[0] = int(z[0])
    z[1] = int(z[1])
    a = li[z[0]]
    li[z[0]] = li[z[1]]
    li[z[1]] = a
for i in li:
    print(i, end=" ")
