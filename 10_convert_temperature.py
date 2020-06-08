def temp(li):
    w = 0
    if li[1] == "Celsius" and li[0] < (-273.15) or li[1] == "Fahrenheit" and li[0] < (-459.67) or li[1] == "Kelvin" and li[0] < 0:
        return "NO"
    if li[1] == "Fahrenheit" and li[2] == "Celsius":
        w = (li[0] - 32) / 1.8
    if li[1] == "Fahrenheit" and li[2] == "Kelvin":
        w = (li[0] + 459.67) * (5/9)
    if li[1] == "Kelvin" and li[2] == "Celsius":
        w = li[0] - 273.15
    if li[1] == "Kelvin" and li[2] == "Fahrenheit":
        w = li[0] * 1.8 - 459.67
    if li[1] == "Celsius" and li[2] == "Fahrenheit":
        w = li[0] * 1.8 + 32
    if li[1] == "Celsius" and li[2] == "Kelvin":
        w = li[0] + 273.15
    return round(w, 2)


while(True):
    try:
        x = input().split()
        x[0] = int(x[0])
        if temp(x) != "NO":
            print("%.2f" % temp(x))
        else:
            print(temp(x))

    except EOFError:
        break