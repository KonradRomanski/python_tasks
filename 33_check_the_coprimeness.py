import math

def GCD(a, b):
    while a%b != 0:
        w = a%b
        a = b
        b = w
    return b


# listw = []
n = int(input())
for i in range(n):
    el = int(input())

    for j in range(math.floor(el/2)):
        if GCD(math.floor(el/2)-j, el) == 1:
            # listw.append(math.floor(el/2)-j)
            print(math.floor(el/2)-j)
            break

# for i in listw: print(i)