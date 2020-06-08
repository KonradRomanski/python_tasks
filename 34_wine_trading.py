def work(listt):
    back = 0
    cost = 0
    for i in enumerate(listt):
        back += i[1]
        cost += abs(back)
        listt[i[0]] = 0
        #print(listt)
        #print(back, cost)
    return cost

def main():
    n = 5
    while True:
        n = int(input())
        if n == 0:
            break

        li = list(map(int, input().split()))
        print(work(li))


main()