def palindr0000m(signs):
    # print(signs)
    if signs[0] == '0': return False

    while(signs[len(signs)-1] == '0'):
        signs = signs[:len(signs)-1]
        # print("%%%")
    # print(signs)
    if signs == signs[::-1]: return True
    return False


def main():
        line = input()
        score = 0
        for i in range(len(line)):
            temp = line
            while len(temp) > 0:
                t = temp[:i+1]
                # print(t)
                if len(t) == i+1 and palindr0000m(t):
                    # print("$$$$$", t)
                    score += 1
                temp = temp[1:]
        print(score)

        # print(palindr0000m("10"))

main()