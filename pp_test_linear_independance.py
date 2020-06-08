def independance(A, B):

    if sum(A) == 0 or sum(B) == 0:
        return False

    for i in range(len(A)):
        if (A[i] == 0 and B[i] != 0) or (B[i] == 0 and A[i] != 0): return False

    # for i in range(1, len(A)):
    #     if B[i-1] != 0 and B[i] != 0:
    #         if not A[i-1]/B[i-1] == A[i]/B[i]: return False
    #     if A[i-1] != 0 and A[i] != 0:
    #         if not B[i-1]/A[i-1] == B[i]/A[i]: return False

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            # print("####", A[i], B[i], A[j], B[j], "|", A[i]/B[i] if B[i]!=0 else [], A[j]/B[j] if B[j]!=0 else [], "^^", A, B, i, j)
            if B[i] != 0 and B[j] != 0:
                if A[i]/B[i] != A[j]/B[j]: return False
            if A[i] != 0 and A[j] != 0:
                if B[i]/A[i] != B[j]/A[j]: return False
    # print("%%", A, B)
    return True


def main():
    size = int(input())
    M = []
    for i in range(size):
        li = list(map(int, input().split()))
        M.append(li)
    M_full = M.copy()
    M_full = M + list(map(list, zip(*M_full)))

    # print(M)
    # print(M_full)
    number_of_independance_vectors = 0
    for i in range(len(M_full)):
        for j in range(i+1, len(M_full)):
            # print(i, j)
            if independance(M_full[i], M_full[j]) == True:
                number_of_independance_vectors += 1

    print(number_of_independance_vectors)



main()