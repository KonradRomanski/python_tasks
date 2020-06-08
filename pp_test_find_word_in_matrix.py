def main():
    a = list(map(int, input().split()))
    word = input()
    m = [[i for i in input()] for j in range(a[0])]
    # print(a, word, m, sep="\n")
    for i in range(a[0]):
        print("".join(m[i]))
        if word in "".join(m[i]) or word[::-1] in "".join(m[i]):
            print("YES")
            return

    for i in range(a[1]):
        # print("".join([m[j][i] for j in range(len(m))]))
        if word in "".join([m[j][i] for j in range(len(m))]) or word[::-1] in "".join([m[j][i] for j in range(len(m))]):
            print("YES")
            return
    print("NO")
    print(a, word, m, sep="\n")


main()

# 3 5
# abc
# qwerc
# dfffb
# wetga