def beated(number, data):
    for i in data:
        # print("$$", i)
        # print("$$", data, number)
        if number[0] == i[0] or number[1] == i[1]: return True
    return False


def abeated(number, data):
    new_data = []
    for i in data:
        if i != number:
            new_data.append(i)
    # print('%%', new_data, number)
    for i in new_data:
        if number[0] == i[0] or number[1] == i[1]: return True
    return False


def main():
    size = 8+2
    szachownica = []
    szachownica.append("##########")
    for i in range(size-2):
        li = input()
        li = '#' + li + '#'
        szachownica.append(li)
    szachownica.append("##########")
    # print(szachownica)

    king = tuple()
    towers = []
    for i in range(size):
        for j in range(size):
            if szachownica[i][j] == 'k':
                king = (i, j)
            if szachownica[i][j] == 'w':
                towers.append((i, j))
    # print(king, towers)
    # print(szachownica[king[0]-1][king[1]], king[0]-1, king[1], king[0]-1 in towers, king[1] in towers, szachownica[king[0]-1][king[1]] in towers, beated(king[0]-1, towers), beated(king[1], towers))
    #pole bezpieczne

    # print(abeated((6, 7), 6, towers))
    if (szachownica[king[0]][king[1]-1] == 'w' and not abeated((king[0], king[1]-1), towers))\
            or (szachownica[king[0]][king[1]+1] == 'w' and not abeated((king[0], king[1]+1), towers))\
            or (szachownica[king[0]-1][king[1]-1] == 'w' and not abeated((king[0]-1, king[1]-1), towers))\
            or (szachownica[king[0]-1][king[1]+1] == 'w' and not abeated((king[0]-1, king[1]+1), towers))\
            or (szachownica[king[0]+1][king[1]-1] == 'w' and not abeated((king[0]+1, king[1]-1), towers))\
            or (szachownica[king[0]+1][king[1]+1] == 'w' and not abeated((king[0]+1, king[1]+1), towers))\
            or (szachownica[king[0]-1][king[1]] == 'w' and not abeated((king[0]-1, king[1]), towers))\
            or (szachownica[king[0]+1][king[1]] == 'w' and not abeated((king[0]+1, king[1]), towers))\
            \
            or (szachownica[king[0]][king[1]-1] == 'o' and not beated((king[0], king[1]-1), towers))\
            or (szachownica[king[0]][king[1]+1] == 'o' and not beated((king[0], king[1]+1), towers))\
            or (szachownica[king[0]-1][king[1]-1] == 'o' and not beated((king[0]-1, king[1]-1), towers))\
            or (szachownica[king[0]-1][king[1]+1] == 'o' and not beated((king[0]-1, king[1]+1), towers))\
            or (szachownica[king[0]+1][king[1]-1] == 'o' and not beated((king[0]+1, king[1]-1), towers))\
            or (szachownica[king[0]+1][king[1]+1] == 'o' and not beated((king[0]+1, king[1]+1), towers))\
            or (szachownica[king[0]-1][king[1]] == 'o' and not beated((king[0]-1, king[1]), towers))\
            or (szachownica[king[0]+1][king[1]] == 'o' and not beated((king[0]+1, king[1]), towers)):

            print("nierozstrzygniete")
    else:
        if beated((king[0], king[1]), towers):
            print('mat')
        else:
            print('pat')



main()