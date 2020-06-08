def main():
    size = int(input())
    line = list(map(int, input().split()))
    data = {}
    for i in range(size+1):
        for j in range(size+1):
            if i != j and line[i:j] != []:
                print(line[i:j])
                print("##_2_##", line[i:j:2], sum(line[i:j:2]))
                if not sum(line[i:j:2]) in data:
                    data[sum(line[i:j:2])] = [0, 0]
                data[sum(line[i:j:2])][0] += 1

                print("##_3_##", line[i:j:3], sum(line[i:j:3]))
                if not sum(line[i:j:3]) in data:
                    data[sum(line[i:j:3])] = [0, 0]
                data[sum(line[i:j:3])][1] += 1
    print(data)
    result = sorted(data.items(), reverse=True)
    print(result)

    num = 0
    while result[num][1][0] == 0 or result[num][1][1] == 0:
        num += 1
    print(result[num][0])

    
main()

# 5
# 5 8 1 2 3

# 9
# 1 2 3 4 5 6 7 8 9