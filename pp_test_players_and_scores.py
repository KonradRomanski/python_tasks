def main():
    number_of_lines = int(input())
    gamers = {}
    for i in range(number_of_lines):
        li = input().split()
        li = [i.split(":") for i in li]
        # print(li)
        if not li[0][0] in gamers: gamers[li[0][0]] = [0, 0]
        if not li[1][0] in gamers: gamers[li[1][0]] = [0, 0]

        if int(li[0][1]) > int(li[1][1]):
            gamers[li[0][0]][0] += 1
        elif int(li[0][1]) < int(li[1][1]):
            gamers[li[1][0]][0] += 1

        gamers[li[0][0]][1] += int(li[0][1])
        gamers[li[1][0]][1] += int(li[1][1])

    # print(gamers)

    sort_1 = sorted(gamers.items(), key=lambda x: x[0])
    sort_2 = sorted(sort_1, key=lambda x: x[1][1], reverse=True)
    sort_3 = sorted(sort_2, key=lambda x: x[1][0], reverse=True)

    # print(sort_1)
    # print(sort_2)
    # print(sort_3)
    for i in sort_3:
        print(i[0])


main()