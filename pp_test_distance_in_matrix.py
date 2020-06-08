def distance(a, b):
    if (b[0]+1)%(a[0]+1) == 0 and (b[1]+1)%(a[1]+1) == 0:
        # print("&&", a, b)
        # print(abs(a[0] - b[0]) + abs(a[1] - b[1]))
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    else:
        return 'nope'


def main():
    size = int(input())
    M = []
    pairs = []
    for i in range(size):
        li = list(map(int, input().split()))
        M.append(li)
    # print(M)
    for i in range(size):
        for j in range(size):
            if M[i][j] == 1:
                pairs.append((i, j))

    # print(pairs)
    ff = 0
    min = 9999999
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            # print(pairs[i], pairs[j])
            if distance(pairs[i], pairs[j]) != 'nope':
                ff = 1
                if distance(pairs[i], pairs[j]) < min:
                    min = distance(pairs[i], pairs[j])
    if ff == 1:
        print(min)
    else:
        print(1000)


main()