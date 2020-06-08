expression = input().lower()
numbers = [0] * 123
for i in expression:
    if (i >= 'a' and i <= 'z'):
        # print(i, "TAK")
        numbers[ord(i)] += 1
    # else:
    #     print(i, "NIE")
# for g in enumerate(numbers):
#     print(g[0],g[1])

maks = -1
li = 0
for h in enumerate(numbers):
    if maks < h[1]:
        maks = h[1]
        li = h[0]
print(chr(li))
# print(expression)