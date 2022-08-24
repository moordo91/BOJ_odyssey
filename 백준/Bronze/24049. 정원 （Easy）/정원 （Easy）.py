n, m = map(int, input().split())
field = [[-1 for _ in range(m+1)] for _ in range(n+1)]
line1 = [0] + list(map(int, input().split()))
line2 = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    field[i][0] = line1[i]
for i in range(1, m+1):
    field[0][i] = line2[i]

for i in range(1, n+1):
    for j in range(1, m+1):
        if field[i-1][j] == field[i][j-1]:
            field[i][j] = 0
        else:
            field[i][j] = 1
print(field[n][m])