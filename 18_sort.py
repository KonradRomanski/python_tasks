n = int(input())
li = input()
li = li.split()
for h in enumerate(li):
    li[h[0]] = int(li[h[0]])
li.sort()
for i in li:
    print(i, end=" ")
