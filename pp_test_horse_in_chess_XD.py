def beating(board, horse_location):
    x, y= horse_location
    tab = board.copy()
    # tab[horse_location[0]][horse_location[1]] = '#'
    tab[x] = tab[x][:y] + '&' + tab[x][y+1:]
    # print(tab, x, y)

    # if tab[x+2][y-1] == 's': return True
    # elif tab[x+2][y+1] == 's': return True
    # elif tab[x+1][y+2] == 's': return True
    # elif tab[x-1][y+2] == 's': return True
    # elif tab[x-2][y+1] == 's': return True
    # elif tab[x-2][y-1] == 's': return True
    # elif tab[x-1][y-2] == 's': return True
    # elif tab[x+1][y-2] == 's': return True
    # return False

    quantity = 0
    if tab[x+2][y-1] == 's': quantity += 1
    if tab[x+2][y+1] == 's': quantity += 1
    if tab[x+1][y+2] == 's': quantity += 1
    if tab[x-1][y+2] == 's': quantity += 1
    if tab[x-2][y+1] == 's': quantity += 1
    if tab[x-2][y-1] == 's': quantity += 1
    if tab[x-1][y-2] == 's': quantity += 1
    if tab[x+1][y-2] == 's': quantity += 1
    return quantity


def main():
    board_size = int(input())
    M = []
    for i in range(board_size):
        M.append(input())
    # for i in range(board_size): print(M[i])

    M_operationable = M.copy()

    for i in range(board_size):
        M_operationable[i] = 'o'*2 + M_operationable[i] + 'o'*2
    M_operationable.insert(0, "o"*(len(M_operationable[0])))
    M_operationable.insert(0, "o"*(len(M_operationable[0])))
    M_operationable.insert(len(M_operationable), "o"*(len(M_operationable[0])))
    M_operationable.insert(len(M_operationable), "o"*(len(M_operationable[0])))
    # for i in range(len(M_operationable)): print(M_operationable[i])

    list_of_horses = []
    for i in range(len(M_operationable)):
        for j in range(len(M_operationable[i])):
            if M_operationable[i][j] == 's':
                list_of_horses.append((i, j))
    # print(list_of_horses)
    quantity_of_beats = 0
    for i in list_of_horses:
        # if beating(M_operationable, i):
        #     print("^^", i)
        #     quantity_of_beats += 1
            quantity_of_beats += beating(M_operationable, i)


    print(quantity_of_beats)

main()

# 5
# ooooo
# oooos
# oooso
# ssooo
# oooso