import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
visited = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            dist[y][x] = 0
            start = (y, x)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(graph, start, visited, dist):
    queue = deque([start])
    y, x = start
    visited[y][x] = True
    dist[y][x] = 0
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or ny >= n or nx < 0 or nx >= m or graph[ny][nx] == 0:
                continue
            if not visited[ny][nx] and graph[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
                
bfs(graph, start, visited, dist)

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1 and not visited[y][x]:
            dist[y][x] = -1
        print(dist[y][x], end=' ')
    print()