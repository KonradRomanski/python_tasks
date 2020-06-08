def main():
    m, n = (int(i) for i in input().split())
    # print(m, n)
    M = []
    for i in range(m):
        li = list(map(int, input().split()))
        M.append(li)
    # print(M)
    number_of_operations = int(input())
    for i in range(number_of_operations):
        li = input().split()

        if li[0] == "T":
            M = list(map(list, list(zip(*M))))

        elif li[0] == "RR":
            for j in range(len(M)):
                if j == int(li[1]):
                    M[j] = M[j][::-1]

        elif li[0] == "RC":
            vector = [M[i][int(li[1])] for i in range(len(M))]
            vector = vector[::-1]
            # print(vector)
            for i in range(len(M)):
                M[i][int(li[1])] = vector[i]

    # print(M)
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=" ")
        print()

main()