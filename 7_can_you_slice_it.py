x = list(map(int, input().split()))
x.sort()
# print(x)
# if len(x)>1:s = abs(x[1]-x[0])
# else: s=0
# print(s)
# w = x[0]
c = True
# for i in range(1, len(x)):
#     w += s
#     if w != x[i]:
#         print("False")
#         c = False
#         break
#     print(w, x[i])

for i in range(len(x)-2):
    if x[i+1]-x[i] != x[i+2]-x[i+1]:
        print("False")
        c = False
        break
    # print(i)

# for i in x:
#     if(i%s != 0):
#         print("False")
#         c = False
if c:
    print("True")
