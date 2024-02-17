import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]
for y in range(n):
    graph.append(list(input()))
    
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start = (i, j)
   
cnt = 0         

def bfs(graph, visited, start):
    global cnt
    queue = deque([start])
    y, x = start
    visited[y][x] = True
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if not visited[ny][nx] and graph[ny][nx] != 'X':
                visited[ny][nx] = True
                if graph[ny][nx] == 'P':
                    cnt += 1
                queue.append((ny, nx))

bfs(graph, visited, start)

if cnt == 0:
    print("TT")
else:
    print(cnt)