arr = [[False for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if not arr[y][x]:
                arr[y][x] = True

ans = 0
for y in range(101):
    for x in range(101):
        if arr[y][x]:
            ans += 1

print(ans)
