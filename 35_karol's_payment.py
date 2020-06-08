def days(money, final_money):
    w = 0
    asa = 0
    while asa < final_money:
        asa += money
        money = 2*money
        w += 1
    return w


t = int(input())
ww = []

for i in range(t):
    l = list(map(int, input().split()))
    ww.append(days(l[0], l[1]))
for i in ww:
    print(i)
