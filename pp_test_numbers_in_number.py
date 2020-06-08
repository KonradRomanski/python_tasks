def main():
    number = input()
    actual_number = number
    times = {}

    for i in range(1, len(number) + 1):
        times = {}
        actual_number = number

        while len(actual_number) > 0:
            a = actual_number[:i]
            if not a in times and int(len(a)) == i: times[a] = 0
            if int(len(a)) == i: times[a] += 1
            actual_number = actual_number[1:]

        maxx = 0
        maxx_number = 0
        for j in times.items():
            if j[1] > maxx:
                maxx = j[1]
                maxx_number = int(j[0])
            elif j[1] == maxx:
                if int(j[0]) < maxx_number:
                    maxx = j[1]
                    maxx_number = int(j[0])

        print(maxx_number)
        # print(times)

    # print(number)
    # print(actual_number)


main()