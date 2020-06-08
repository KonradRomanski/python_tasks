def ceasar(p, c):
    w = ""
    for i in enumerate(c):
        if  ord(i[1]) >= 65 and ord(i[1]) <= 90:
            w+= chr((ord(i[1])-65- p )%26 +65)
        elif(ord(i[1]) >= 97 and ord(i[1]) <= 122):
            w+= chr((ord(i[1]) - 97 - p) % 26 + 97)
    return w

x = int(input())
li = input()
print (ceasar(x, li))
# d = (ord("A")-65- 3 )%26 +65
# print(d)
# print(chr(d))