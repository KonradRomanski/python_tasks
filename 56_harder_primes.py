def prime(a):
    if a < 2 or (a % 2 == 0 and a > 2):
        return False

    for i in range(3, int(a ** (1 / 2)) + 1, 2):
        if a % i == 0:
            return False
    return True


def main():
    n = int(input())

    primes = []
    for i in range(100000):
        primes.append(1)

    for i in range(100000):
        if primes[i] == 1 and prime(i) == False:
            primes[i] = 0
        # print(i, primes[i])

    for i in range(n):
        a = int(input())
        if primes[a] == 1:
            print("YES")
        else:
            print("NO")


main()