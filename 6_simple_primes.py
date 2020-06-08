def prime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def main():
    n = int(input())

    for i in range(2, n + 1):
        if prime(i):
            print(i)


main()
