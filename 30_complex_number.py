import math


def ar(r, i):
    r = float(r)
    i = float(i)
    if r > 0:
        return math.atan(i/r)
    elif r < 0 and i >= 0:
        return math.atan(i/r) + math.pi
    elif r < 0 and i < 0:
        return math.atan(i/r) - math.pi
    elif r == 0 and i > 0:
        return math.pi / 2
    elif r == 0 and i < 0:
        return math.pi/2
    else:
        return 0


li = input().split()
li.remove(li[1])
li[1] = li[1].replace('j', '')
a = int(li[0])
b = int(li[1])
# print(a, b)
mod = round((a*a + b*b)**(1/2),4)
if int(mod) == mod: mod = int(mod)
argu = round(ar(a, b),4)
if int(argu) == argu: argu = int(argu)
print(mod, argu, sep='\n')
