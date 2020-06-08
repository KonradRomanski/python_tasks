class cat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    def __lt__(self, other):
        if self.x < other.x:
            return True
        else: return False

    # def __gt__(self, other):
    #     if self.x > other.x:
    #         return False


def main():
    a = [1, 2, 3, 4, 5, 6]
    b = ['q', 'w', 'e', 'r', 't', 'y']
    # print(f'a: {a}, {"".join(a)}')
    print(f'b: {b}')

    A = cat(58888, 10)
    B = cat(555, 1000)
    print(A < B)

    M = ['12345', '67890', '11223', '34455', '66778']
    for i in range(len(M)): print(M[i])
    for i in range(1, len(M)-1):
        for j in range(1, len(M[i])-1):
            print(M[i][j], end='')
        print()



main()