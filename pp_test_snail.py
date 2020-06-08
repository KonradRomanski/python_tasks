def main():
    size = int(input())
    M = []
    for i in range(size):
        li = list(map(int, input().split()))
        M.append(li)
    # print(M)
    result = []
    up = 0
    down = size - 1
    left = 0
    right = size - 1
    while len(result) < size**2:
        result += (M[up][left:right+1])
        up += 1
        if len(result) >= size ** 2: break

        result += ([M[i][right] for i in range(up, down)])
        right -= 1
        if len(result) >= size ** 2: break

        result += (M[down][left:right+2][::-1])
        down -= 1
        if len(result) >= size ** 2: break

        result += ([M[i][left]for i in range(down, up-1, -1)])
        left += 1
        if len(result) >= size**2: break

    # print(result)
    for i in result:
        print(i, end = " ")

main()