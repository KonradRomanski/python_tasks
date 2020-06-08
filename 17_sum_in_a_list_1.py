x = input()
x = x.split()
n = input()
n = n.split()
i = int(n[0])
j = int(n[1])
w = 0
for g in range(i, j+1):
    w += int(x[g])
print(w)
