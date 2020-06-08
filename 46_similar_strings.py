def sim(x, y):
    f = False
    if x == y or x[:-1] == y: return True
    for i in range(len(x)):
        if x[i] != y[i] and f == False:
            f = True
            y = y[:i]+x[i]+y[i:]
        if x[i] != y[i] and f == True:
            return False
    return True

# def sim(x, y):
#     if x == y or x[:-1] == y: return True
#     for i in range(len(x)):
#         if x[:i]+x[i+1:] == y: return True
#         if x[:(-1)*(i+1)]+x[(-1)*(i):] == y: return True
#     return False


def main():
    a = input()
    b = input()
    if sim(a, b): print("TAK")
    else: print("NIE")


main()