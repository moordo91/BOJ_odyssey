from collections import deque
import sys; gets = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
ocean = [list(map(int, gets().split())) for _ in range(n)]

def sol(y, x, n):
    q = deque([(y, x)])
    
    vnd = [[-1 for _ in range(n)] for _ in range(n)]
    vnd[y][x] = 0

    prey = []

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= nx < n and 0 <= ny < n and vnd[ny][nx] < 0):
                continue

            if ocean[ny][nx] <= shark:
                q.append((ny, nx))
                vnd[ny][nx] = vnd[y][x] + 1
                if 0 < ocean[ny][nx] < shark:
                    prey.append((vnd[ny][nx], ny, nx))
    
    return sorted(prey, key=lambda p: (-p[0], -p[1], -p[2]))


for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            ocean[i][j] = 0
            y, x = i, j

shark = 2
exp = 0
t = 0

while 1:
    prey = sol(y, x, n)
    if not prey:
        break
    
    else:
        prey = prey.pop()

        ocean[y][x] = 0
        t += prey[0]
        y, x = prey[1], prey[2]

        exp += 1

        if exp == shark:
            shark += 1
            exp = 0

print(t)