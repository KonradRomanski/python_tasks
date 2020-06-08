def good(wektor):
    numbers = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    # print(numbers)
    for i in range(len(wektor)):
        numbers[wektor[i]] += 1
    # print(numbers)

    for i in numbers.items():
        if i[1] != 1: return False
    return True

def main():
    sudoku = []
    for i in range(9):
        li = list(map(int, input().split()))
        sudoku.append(li)
    # print(sudoku)

    for i in sudoku:
        if not good(i):
            print(False)
            return

    diagonal_1 = [sudoku[i][i] for i in range(9)]
    diagonal_2 = [sudoku[i][8-i] for i in range(9)]
    # print(diagonal_1, diagonal_2)

    sudoku = list(map(list, zip(*sudoku)))
    # print(sudoku)

    for i in sudoku:
        if not good(i):
            print(False)
            return

    if good(diagonal_1) and good(diagonal_2):
        print("X")
        return
    else:
        print(True)
        return

    # good(diagonal_2)

main()