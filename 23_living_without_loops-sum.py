def su(a, b):
    if a == -1:
        return 0
    else:
        return su(a-1, b) + int(b[a])


# x = int(input())
# li  = input().split().map(lambda x : int(x))
li = input().split()
# li = list(map(int, input().split()))
# print(li[0])
x = len(li)
print(su(x-1, li))
