def troj(x, y, z):
    if x + y > z and x + z > y and z + y > x:
        return True
    return False


def main():
    T = {}
    P = {}
    n = int(input())
    for i in range(n):
        li = input().split()
        a = int(li[1])
        b = int(li[2])
        c = int(li[3])
        T[li[0]]=[a, b, c]
        if troj(a, b, c):
            p = (1/2) * (a + b + c)
            P[li[0]] = int((p * (p - a) * (p - b) * (p - c) )**(1/2))
        else: P[li[0]] = 0
    A = sorted(P, key=lambda x: P[x])
    # print(T)
    # print(P)
    # print(A)
    NONE = []
    W = {}
    for i in A:
        if not P[i] in W:
            W[P[i]] = []
        W[P[i]].append(i)
    # print(W)
    for i in W.items():
        if not i[0] == 0:
            print(f"{i[0]}: ", end="", sep="")
        for j in i[1]:
            if i[0] == 0:
                NONE.append(f"Trojkat {j} jest zadany niepoprawnie")
            if not i[0] == 0:
                print(j, end=" ", sep="")
        print()
    for i in NONE:
        print(i)
main()