s = input()
print(f"{int(s) > 1 and all(int(s) % i for i in range(2, int(int(s)**(1/2)) +1))}")