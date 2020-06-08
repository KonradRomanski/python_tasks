def lower(ll):
    w = 0
    ma = 0
    for i in enumerate(ll):
        # print(ll)
        for j in range(i[0] + 1, len(ll)):
            # print("##", i[0], j, ll[j-1], ll[j], "   ", w)
            if ll[j-1] >= ll[j]:
                w += 1
                # print("www ", w)
            else:
                break

        if ma < w:
            ma = w
        w = 0
    return ma


n = int(input())
li = list(map(int, input().split()))
print(lower(li))
