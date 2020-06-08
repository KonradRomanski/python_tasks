def sequence(o, n, it, a, ta):
    ta += str(n) + " "
    if n < 0: a = True
    if o != n - it and a == False:
        return sequence(o, n - it, it, a, ta)
    elif o != n + it and a == True:
        return sequence(o, n + it, it, a, ta)
    elif o == n + it and a == True:
        ta += str(n+it)
        return ta


x = input().split()
a = False
tab = ""
tab = sequence(int(x[0]), int(x[0]), int(x[1]), a, tab)
print(tab)