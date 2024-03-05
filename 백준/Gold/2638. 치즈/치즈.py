import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if grid[nx][ny] >= 1:
                    grid[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
answer = 0
while 1:
    visited = [[0]*m for _ in range(n)]
    bfs()
    flag = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] >= 3:
                grid[i][j] = 0
                flag = 1
            elif grid[i][j] == 2:
                grid[i][j] = 1
    if flag == 1:
        answer += 1
    else:
        break

print(answer)