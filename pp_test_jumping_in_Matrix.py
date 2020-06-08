class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Co-ordinates [x, y]: {self.x}, {self.y}"


def main():
    dimension = int(input())
    li = [int(i) for i in input().split()]
    start_pos = Point(li[0], li[1])
    actual_pos = start_pos
    m = [[0 for i in range(dimension)] for j in range(dimension)]

    for i in range(dimension):
        l = [int(a) for a in input().split()]
        for j in range(dimension):
            m[i][j] = l[j]
    # print(m, actual_pos, sep="\n")

    # u = [m[i][2] for i in range(dimension)]
    # print(u)

    while (min(m[actual_pos.x]) != m[actual_pos.x][actual_pos.y]) or (min([m[i][actual_pos.y] for i in range(dimension)]) != m[actual_pos.x][actual_pos.y]):

        if m[actual_pos.x][actual_pos.y] != min(m[actual_pos.x]):
            actual_pos.y = m[actual_pos.x].index(min(m[actual_pos.x]))
            # print(actual_pos)

        elif m[actual_pos.x][actual_pos.y] != min([m[i][actual_pos.y] for i in range(dimension)]):
            actual_pos.x = [m[i][actual_pos.y] for i in range(dimension)].index(min([m[i][actual_pos.y] for i in range(dimension)]))
            # print(actual_pos)
    print(actual_pos.x, actual_pos.y)

main()
