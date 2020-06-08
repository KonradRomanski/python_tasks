import math
def blind(n):
    t = ""
    if n == 1: return "poor conductor"
    else: 
        t += str(math.ceil((n-1)/5))
        if (n-1)%10 == 0 or (n-1)%10 == 1: t += " W L"
        if (n-1)%10 == 2 or (n-1)%10 == 9: t += " A L"
        if (n-1)%10 == 3 or (n-1)%10 == 8: t += " A R"
        if (n-1)%10 == 4 or (n-1)%10 == 7: t += " M R"
        if (n-1)%10 == 5 or (n-1)%10 == 6: t += " W R"

        return t

t = int(input())
w = []

for i in range(t):
    w.append(blind(int(input())))

for i in w: print(i)
# 1 2 3 4 5
# 0 9 8 7 6