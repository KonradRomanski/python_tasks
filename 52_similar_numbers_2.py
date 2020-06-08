A = {}
B = {}
n = int(input())
li = input().split()
for i in li: A[int(i)] = True
B = A.copy()
# li = list(map(int, input().split()))
c = False
# a = 0
for i in A.keys():
    if (i+1 in B) or (i-1 in B):
        print("YES")
        c = True
        break

# for i in li:
#     for j in li[a:]:
#         if i == j+1 or i+1 == j:
#             print("YES")
#             c = True
#             break
#         if c == True:
#             break
#     a += 1
if c == False:
    print("NO")

# n = int(input())
# li = input().split()
# for i in enumerate(li): li[i[0]] = int(li[i[0]])
# c = False
# a = 0
# for i in li:
#     for j in li[a:]:
#         if i == j+1 or i+1 == j:
#             print("YES")
#             c = True
#             break
#         if c == True:
#             break
#     a += 1
# if c == False:
#     print("NO")
