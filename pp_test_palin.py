def palindrom(a):
    B = ""
    for i in range(len(a) - 1, -1, -1):
        B += a[i]
    if B == a:
        return True
    else:
        return False


def pp(s):
    if palindrom(s):
        return True

    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        if palindrom(t):
            return True

    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        for j in range(len(t)):
            t2 = t[:j] + t[j + 1:]
            if palindrom(t2):
                return True
    return False


def main():
    p = input()
    pn = p.lower()

    if pp(pn):
        print("YES")
    else:
        print("NO")


main()