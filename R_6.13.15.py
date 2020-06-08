# Calculate an approximation of PI using the Leibniz
# approximation with iters number of iterations

# your code here


def myPi(g):
    w = 1.0
    c = 3
    z = -1
    b = (z * 1) / c
    z *= (-1)
    s = 1.5
    # print("w " + str(w), "c " + str(c), "s " + str(s))
    while(abs(s - w) >= g):
        s = w
        w += b
        c += 2
        b = 1 / c
        b *= z
        z *= (-1)
        # print("w " + str(w), "c " + str(c), "s " + str(s))

    w *= 4
    return w


print(myPi(0.00000001))
