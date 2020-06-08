n = int(input())
li = input().split()
for i in enumerate(li): li[i[0]] = int(li[i[0]])
c = False
for i in li:
    for j in li:
        if i == j+1 or i+1 == j:
            print("YES")
            c = True
            break
        if c == True:
            break
if c == False:
    print("NO")
