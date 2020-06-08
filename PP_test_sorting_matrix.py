U = [[5, 3, 7], [9, 6, 2], [3, 6, 0]]
U_new = [U[i][j] for i in range(len(U)) for j in range(len(U[i]))]
U_new = sorted(U_new)


U_connected = [[U_new[j+len(U[i])*i] for j in range(len(U[i]))] for i in range(len(U))]

U_inv = [[U_connected[j][i] for j in range(len(U_connected[i]))] for i in range(len(U_connected))]
U_inv = list(map(list, zip(*U_connected)))

print(U, U_new, sep="\n")

print(U_connected)
print(U_inv)
