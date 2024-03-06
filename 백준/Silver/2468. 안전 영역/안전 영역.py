import sys, copy
from collections import deque
input = sys.stdin.readline

n = int(input())
region = [list(map(int,input().split())) for _ in range(n)]
max_height = max(max(row) for row in region)

def bfs(after_rain, start):
    global visited
    queue = deque([start])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and after_rain[ny][nx] != 0:
                queue.append((ny, nx))
                visited[ny][nx] = True

count_list = [1]
for i in range(max_height+1):
    after_rain = copy.deepcopy(region)
    for y in range(n):
        for x in range(n):
            if after_rain[y][x] <= i:
                after_rain[y][x] = 0
    visited = [[False]*n for _ in range(n)]
    count = 0
    for y in range(n):
        for x in range(n):
            if not visited[y][x] and after_rain[y][x] != 0:
                bfs(after_rain, (y, x))
                count += 1
    count_list.append(count)

print(max(count_list))
            
                
    