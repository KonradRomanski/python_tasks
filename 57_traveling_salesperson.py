def main():
    M = {}
    n = int(input())
    for i in range(n):
        li = input().split()
        if not li[0] in M: M[li[0]] = [0, 0]
        M[li[0]]= [int(li[1]), int(li[2])]
    # print(M)
    way = input().split()
    way = way + [way[0]]
    # print(way)
    point = [M[way[0]][0], M[way[0]][1]]
    sum = 0
    for i in way:
        # sum += abs(point[0] - M[i][0]) + abs(point[1] - M[i][1])
        # print(sum)
        sum += ((point[0] - M[i][0])**2 + (point[1] - M[i][1])**2)**(1/2)
        point = [M[i][0], M[i][1]]
    print("{0:0.3f}".format(sum))



main()