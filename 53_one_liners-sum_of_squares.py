s = input()

# print(f"{sum(j**2 for x, i in enumerate(list(map(int, s.split()))) if x !=0 for j in range(i+1))}")
print(f"{sum(i**2 for i in range(list(map(int, s.split()))[0], list(map(int, s.split()))[1]+1))}")
s = list(map(int, s.split()))
print()
w = 0
for i in s:
    for j in range(i+1):
        print(j, j*j)
        w +=j*j
print(w)