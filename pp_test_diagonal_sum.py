def main():
    rows_quantity, column_quantity = list(map(int, input().split()))
    M = []

    for i in range(rows_quantity):
        li = list(map(int, input().split()))
        M.append(li)
    # print(M)
    M_diagonals_1 = M.copy()
    M_diagonals_2 = M.copy()

    for i in range(rows_quantity):
        M_diagonals_1[i] = [0]*(i) + M_diagonals_1[i] + [0]*(rows_quantity-1-i)
        M_diagonals_2[i] = [0]*(rows_quantity-1-i) + M_diagonals_2[i] + [0]*(i)

    # print(M_diagonals_1)
    # print()
    #
    # for i in range(rows_quantity):
    #     for j in range(column_quantity + rows_quantity - 1):
    #         print(M_diagonals_1[i][j], end=" ")
    #     print()
    # print()
    # for i in range(rows_quantity):
    #     for j in range(len(M_diagonals_2[i])):
    #         print(M_diagonals_2[i][j], end=" ")
    #     print()

    maxx = -999999999
    for i in range(column_quantity + rows_quantity - 1):
        temporary_sum = sum([M_diagonals_1[k][i] for k in range(rows_quantity)])
        # print(temporary_sum)
        if temporary_sum > maxx: maxx = temporary_sum

        temporary_sum = sum([M_diagonals_2[k][i] for k in range(rows_quantity)])
        if temporary_sum > maxx: maxx = temporary_sum
    print(maxx)

main()