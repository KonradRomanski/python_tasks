def picture(m, found_row, found_column, pictures_rows, pictures_columns, wall_rows, wall_columns):
    # print("$$", found_row, found_column)
    # print("$$$", found_row, found_column,  wall_rows - pictures_rows, wall_columns - pictures_columns)
    if found_row > wall_rows - pictures_rows or found_column > wall_columns - pictures_columns:
        return False
    # print("___))")
    for i in range(wall_rows):
        for j in range(wall_columns):
            if i >= found_row and j >= found_column and m[i][j] == 1 and i <= found_row + pictures_rows - 1 and j <= found_column + pictures_columns-1:
                return False
    return True


def main():
    wall_rows, wall_columns, pictures_rows, pictures_columns = list(map(int, input().split()))

    M = []
    for i in range(wall_rows):
        li = [int(k) for k in input().split()]
        M.append(li)
    # print(M)

    for i in range(wall_rows):
        for j in range(wall_columns):
            if M[i][j] == 0:
                if picture(M, i, j, pictures_rows, pictures_columns, wall_rows, wall_columns):
                    print(True)
                    return True
    print(False)
    return False

main()

# picture size
# matrix size
# matrix

# 2 3
# 4 4
# 1 1 0 1
# 1 0 0 0
# 1 0 0 0
# 1 1 1 1

# 2 3
# 4 4
# 1 0 0 1
# 1 0 0 0
# 1 0 0 1
# 1 1 1 1

# 2 3
# 4 5
# 1 0 1 1 1
# 1 0 0 1 0
# 0 0 0 0 1
# 1 1 1 1 0

# 3 4 2 3
# 1 0 0 1
# 0 0 0 0
# 1 0 0 0