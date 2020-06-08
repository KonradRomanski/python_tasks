def f(k):
    T = []
    for i in range(k + 1):
        T.append(0)
    T[1] = 1

    for i in range(2, k + 1):
        T[i] = 1 + T[i - T[T[i - 1]]]
        if i == k:
            return T[i]


def main():
    n = int(input())
    print(f(n))


main()