x = input() #"Removing vowels!"
y = ""
c = True
v = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
for i in enumerate(x):
    for j in enumerate(v):
        # print(x[i[0]], v[j[0]])
        if x[i[0]] == v[j[0]]:
            c = False
    if c == True:
        y += x[i[0]]
    c = True
            # print("x")
            # print(i[0], i[1])
            # x = x.replace(i[1], ' ')
print(y)
