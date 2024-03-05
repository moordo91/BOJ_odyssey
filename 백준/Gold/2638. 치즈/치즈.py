import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bfs(visited, n, m):
    queue = deque([(0, 0)])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<n and 0<=nx<m and visited[ny][nx] == 0:
                if grid[ny][nx] >= 1:
                    grid[ny][nx] += 1
                else:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

answer = 0

while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    bfs(visited, n, m)
    flag = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] >= 3:
                grid[i][j] = 0
                flag = 1
            elif grid[i][j] == 2:
                grid[i][j] = 1
    if flag:
        answer += 1
    else:
        break

print(answer)