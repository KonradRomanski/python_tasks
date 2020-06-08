x = int(input())
w = 1
if x == 1:
    print(x)
else:
    w = 2
    while (x % w) != 0:
        w += 1
print(w)