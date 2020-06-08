x = list(map(int, input().split()))
a1 = x[0]
a2 = x[1]
x = list(map(int, input().split()))
b1 = x[0]
b2 = x[1]
x = list(map(int, input().split()))
c1 = x[0]
c2 = x[1]

# print(a1, a2)
# print(b1, b2)
# print(c1, c2)
# if a1 == 0 or b1 == 0 or c1 == 0:
#     a = 0
# else:
#     a = ((a2 - b2) / (a1 - b1))
# b = a2 - (a1*a)
# y = (a*c1 + b)

# w = a1*b2 + b1*c2 + b1*a2
# w -= a1*c2 + b1*a2 + x1*b2

# if y == c2:
#     print("True")
# else:
#     print("False")

if b2 - a2 == 0 and c2 - a2 ==0:
    print("True")
elif b2 - a2 == 0 or c2 - a2 ==0:
    print("False")
elif (b1 - a1) / (b2 - a2) == (c1 - a1) / (c2 - a2):
    print("True")
else:
    print("False")