x = input()
x = x.split()
j = int(x[0])
b = int(x[1])
if j > b:
    print("John")
elif j < b:
    print("Betty")
else:
    print("NOBODY")
