def hour(h, t):
    t = int(t)
    h = h[:-1]
    h = list(map(int, h.split(":")))
    h[1] += t
    if h[1] >= 60:
        h[0] += h[1]//60
        h[1] -= (h[1]//60)*60
    # print(h, t)
    h[0] = str(h[0])
    h[1] = str(h[1])

    if h[0] == '0': h[0] = '00'
    elif len(str(h[0])) == 1: h[0] = '0' + h[0]

    if h[1] == '0': h[1] = '00'
    elif len(str(h[1])) == 1: h[1] = '0' + h[1]

    result = h[0] + ":" + h[1]
    return result


def comp(h_1, h_2):
    h_1 = list(map(int, h_1.split(":")))
    h_2 = list(map(int, h_2.split(":")))
    # print("&&&", h_1, h_2)
    if h_1[0] < h_2[0]: return True
    elif h_1[0] > h_2[0]: return False
    elif h_1[0] == h_2[0]:
        if h_1[1] < h_2[1]: return True
        elif h_1[1] > h_2[1]: return False
        else: return False



def main():
    quantity_of_trains, quantity_of_informations = list(map(int, input().split()))
    # print(quantity_of_trains, quantity_of_informations)
    trains = {}
    informations = {}
    for i in range(quantity_of_trains):
        li = input().split()
        trains[(li[7], li[10][:-1])] = li[3][:-1]
    print(trains)

    for i in range(quantity_of_informations):
        li = input().split()
        # print(li)
        if (li[8], li[11]) in informations:
            if comp(informations[(li[8], li[11])], hour(li[3], li[17])):
                informations[(li[8], li[11])] = hour(li[3], li[17])
        else:
            informations[(li[8], li[11])] = hour(li[3], li[17])
    print(informations)

    tab = sorted(trains.items(), key=lambda x: x[1])
    print(tab)

    for i in tab:
        if i[0] in informations:
            print(informations[i[0]])

main()


# 3 5
# Pociag o nazwie 5, jadacy ze stacji C do stacji D.
# Pociag o nazwie abc, jadacy ze stacji X do stacji Y.
# Pociag o nazwie 2, jadacy ze stacji A do stacji B.
# Komunikat z godziny 01:00: Pociag jadacy ze stacji A do stacji B przyjedzie nie wczesniej niz za 85 minut.
# Komunikat z godziny 07:00: Pociag jadacy ze stacji C do stacji D przyjedzie nie wczesniej niz za 0 minut.
# Komunikat z godziny 05:10: Pociag jadacy ze stacji C do stacji D przyjedzie nie wczesniej niz za 55 minut.
# Komunikat z godziny 02:55: Pociag jadacy ze stacji X do stacji Y przyjedzie nie wczesniej niz za 38 minut.
# Komunikat z godziny 12:55: Pociag jadacy ze stacji X do stacji Y przyjedzie nie wczesniej niz za 35 minut.
