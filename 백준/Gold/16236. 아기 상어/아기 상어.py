import sys; gets = sys.stdin.readline
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

shark = 2
time = 0
start = (0, 0)
feed_cnt = 0

n = int(input())
ocean = [list(map(int, gets().split())) for _ in range(n)]

for y in range(n):
    for x in range(n):
        if ocean[y][x] == 9:
            ocean[y][x] = 0
            start = (y, x)
    
def sol(dest, start, n):
    y, x = start
    fish_list = []
    vnd = [[-1 for _ in range(n)] for _ in range(n)] # 해당 칸을 방문했는지(Visited) 그리고(aNd) 방문했다면 얼마나 멀리 떨어진 곳인지(Distance) 나타내는 2차원 리스트
    q = deque([(y, x)])
    vnd[y][x] = 0

    while q and dest:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue 

            if vnd[ny][nx] < 0 and ocean[ny][nx] <= shark:
                vnd[ny][nx] = vnd[y][x] + 1
                q.append((ny, nx))
                if (ny, nx) in dest:
                    fish_list.append((vnd[ny][nx], (ny, nx)))
                    dest.remove((ny, nx))

    return fish_list

while 1:
    dest = []
    for y in range(n):
        for x in range(n):
            if 0 < ocean[y][x] < shark:
                dest.append((y, x))
    if not dest:
        print(time)
        break
    
    else:
        fish_list = sol(dest, start, n)
        if not fish_list:
            print(time)
            break
        target = min(fish_list)
        ocean[target[1][0]][target[1][1]] = 0
        time += target[0]
        start = target[1]
        feed_cnt += 1
    
    if feed_cnt == shark:
        shark += 1
        feed_cnt = 0
