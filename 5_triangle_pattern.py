def triangle(h, n):
    w = ""
    for i in range(n):
        for j in range(h):
            if w == "":
                w = w + "*"
            else:
                w = w + " *"
            print(w)
        h += 1
        w = ""


x = int(input())
y = int(input())
triangle(x, y)
