def main():
    quantity_of_rows, quantity_of_columns = list(map(int, input().split()))
    M = []
    for i in range(quantity_of_rows):
        M += list(map(int, input().split()))
    # print(M)
    M = sorted(M)
    # print(M)
    result = []
    for i in range(quantity_of_rows):
        ll = M[i*quantity_of_columns : i*quantity_of_columns + quantity_of_columns]
        result.append(ll)
    # print(result)
    result_r = result.copy()
    u = 0
    for i in range(quantity_of_columns):
        for j in range(quantity_of_rows):
            result_r[j][i] = M[u]
            u += 1

    # result = list(map(list, zip(*result)))
    # print(result)

    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end = " ")
        print()

main()