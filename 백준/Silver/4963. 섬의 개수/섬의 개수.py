import sys
from collections import deque
input = sys.stdin.readline
dy = [0, 0, 1, -1, 1, -1, 1, -1]
dx = [1, -1, 0, 0, 1, -1, -1, 1]
def sol(y, x):
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and ocean[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = True

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    ocean = [list(map(int, input().split())) for _ in range(h)] 
    visited = [[False]*w for _ in range(h)]
    count = 0
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and ocean[y][x] == 1:
                sol(y, x)
                count += 1
    print(count)