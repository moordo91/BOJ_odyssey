arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))

ans = 0
row, column = (1, 1)

for y in range(9):
    for x in range(9):
        if arr[y][x] > ans:
            ans = arr[y][x]
            row = y+1
            column = x+1

print(ans)
print(row, column)