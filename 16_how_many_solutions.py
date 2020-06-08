l = list(map(int, input().split()))
n = l[0]
x = l[1]
y = l[2]
w = 0


for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            for d in range(n+1):
                if (x*a*a + y*b*b) == (x*c*c + y*d*d):
                    w += 1
print(w)
