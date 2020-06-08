s = input()
# s = list(map(int, s.split()))
# w = 0
# for i in s: if i%2 == 0 and i > 0: w += i
# print(w)
# s = "-2 -1 1 2"
# print(f"{sum(x for x, i in enumerate(list(map(int, s.split()))) if x%2 == 0 and x > 0)}")
print(f"{sum(i for i in list(map(int, s.split())) if i%2 == 0 and i > 0)}")
# print(list(map(int, s.split())))
