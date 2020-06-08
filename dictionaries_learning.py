A = {3 : 'ddd',
     2 : '3333'}
print(2 in A)
print(1 in A)
print('ddd' in A)

print(A.get(3))
print(A[3])

print("\n#####")
for i in A: print(i)
print("#####")
print("\n#####")
for i in A: print(A[i])
print("#####")
print("\n#####")
for i in A.values(): print(i)
print("#####")
print("\n#####")
for i in A.items(): print(i)
print("#####")

print(A)
# A.clear()
del A[2]
#A.popitem() #or pop()
print(A)

B = A.copy() #or dict()
print(B)