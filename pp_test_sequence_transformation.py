def main():
    li = list(map(int, input().split()))
    llen = li[0]
    quantity = li[1]
    signs = input()
    the_longest_string = signs
    for i in range(quantity):
        li = input().split(";")
        li[0] = int(li[0])
        li[1] = int(li[1])
        signs = signs[:(li[0] if li[0] <= li[1] else li[1])] + li[2] + signs[(li[0] if li[0] >= li[1] else li[1]) + 1:]
        if len(the_longest_string) < len(signs):
            the_longest_string = signs
    print(signs)
    print(the_longest_string)


main()