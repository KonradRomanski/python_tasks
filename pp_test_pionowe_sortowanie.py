def main():
    quantity_of_column, quantity_of_rows = list(map(int, input().split()))
    # print(quantity_of_column, quantity_of_rows)
    M = []
    for i in range(quantity_of_rows):
        li = list(map(int, input().split()))
        M.append(li)
    # print(M)
    M = list(map(list, (zip(*M))))
    # print(M)
    for i in range(quantity_of_column):
        M[i] = sorted(M[i])
    # print(M)
    M = list(map(list, (zip(*M))))
    # print(M)

    for i in range(quantity_of_rows):
        for j in range(quantity_of_column):
            print(M[i][j], end = " ")
        print()

main()