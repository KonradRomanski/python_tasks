n = int(input())
g = 0
d = 0
for i in range(n):
    h = int(input())
    if i == 0:
        d = h
    elif d != h:
        g = 1
if g == 0:
    print("True")
else:
    print("False")