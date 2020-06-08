line = input() + '0'
h = 0
il = 0
for i in enumerate(line):
    # print(i)
    if i[0] == 0:
        let = i[1]
        wl = let
    elif i[1] == let:
        h += 1
    else:
        if il < h:
            il = h
            wl = let
        h = 1
        let = i[1]
print(wl)