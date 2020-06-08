def area(a, b, c):
    x1 = b[0] - a[0]
    y1 = b[1] - a[1]

    x2 = c[0] - a[0]
    y2 = c[1] - a[1]

    return abs(x1*y2 - y1*x2)/2


def main():
    quantity = int(input())
    points = []
    for i in range(quantity):
        a = list(map(int, input().split()))
        points.append(a)

    min_area = 9999999999
    max_area = -9999999999

    for i in range(quantity):
        for j in range(quantity):
            for k in range(quantity):
                ar = area(points[i], points[j], points[k])
                if ar != 0:
                    if ar < min_area: min_area = ar
                    if ar > max_area: max_area = ar

    # print(points)
    # print(area(points[0], points[1], points[2]))
    print(min_area, max_area)

main()