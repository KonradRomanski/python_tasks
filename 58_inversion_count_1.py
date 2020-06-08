n = int(input())
A = []
for i in range(n):
	A.append(int(input()))
w = 0
for i in range(n):
	for j in range(n):
		if i < j and A[i] > A[j]:
			w += 1
print(w)