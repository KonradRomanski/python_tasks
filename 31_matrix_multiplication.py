l = list(map(int, input().split()))
w1 = l[0]
h1 = l[1]
m1 = []
m2 = []
m3 = []
# print(w1, h1)
for i in range(h1):
    l = list(map(int, input().split()))
    m1.append(l)

l = list(map(int, input().split()))
w2 = l[0]
h2 = l[1]
# print(w1, h1)
for i in range(h2):
    l = list(map(int, input().split()))
    m2.append(l)
# print(m1, m2)
# print(m2[0][2])
w3 = w2
h3 = h1
u = []
for i in range(h3):
    for j in range(w3):
        act = 0
        for k in range(w1):
            act += m1[i][k]*m2[k][j]
            # print(act, "   lll")
            # print("k i", k, i)
            # print("m1", m1[i][k])
            # print("m2", m2[k][j])
        u.append(act)
        # print("##", act)
    m3.append(u)
    u = []

# print(m3)
for i in range(h3):
    for j in range(w3):
        print(m3[i][j], end=" ")
    print(end="\n")

# 2 3
# 1 2
# 3 4
# 5 6
# 4 2
# 1 2 3 4
# 5 6 7 8