def GCD(a, b):
    while a%b != 0:
        w = a%b
        a = b
        b = w
    return b



w = []
x = int(input())
ww = 0
www = []
for i in range(x):
    li = list(map(int, input().split()))
    li = li[1:len(li)]
    
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            # print("##  ",li[i], li[j], GCD(li[i], li[j]))
            w.append(GCD(li[i], li[j]))
    for i in w: ww += i
    www.append(ww)
    ww = 0
    w = []
for i in www: print(i)