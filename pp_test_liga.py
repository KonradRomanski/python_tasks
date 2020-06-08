def main():
    quantity_of_teams, quantity_of_data, quantity_of_minimum_win_games = list(map(int, input().split()))
    teams = {}
    for i in range(quantity_of_teams):
        #(win_games, games_played)
        teams[input()] = [0, 0]
    # print(teams)

    for i in range(quantity_of_data):
        li = input().split(":")
        li[2] = int(li[2])
        li[3] = int(li[3])
        teams[li[0]][1] += 1
        teams[li[1]][1] += 1
        if li[2] > li[3]:
            teams[li[0]][0] += 1
        else:
            teams[li[1]][0] += 1
    # print(teams)

    result = []
    for i in teams.items():
        if ((quantity_of_teams - 1) - i[1][1] + i[1][0]) >= quantity_of_minimum_win_games:
            result.append(i[0])

    result = sorted(result)

    for i in result:
        print(i)

main()