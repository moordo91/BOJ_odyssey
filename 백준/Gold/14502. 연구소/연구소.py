import sys; gets = sys.stdin.readline
from collections import deque
import copy
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs_and_check(n, m, graph):
    
    q = deque()
    graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i, j))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < n and 0 <= nx < m):
                continue
            
            if graph[ny][nx] == 0:
                graph[ny][nx] = 2
                q.append((ny, nx))
    
    global ans
    cnt_0 = 0

    for i in range(n):
        cnt_0 += graph[i].count(0)
    
    ans = max(ans, cnt_0)

def wall_dfs(cnt, n, m, graph):
    if cnt == 3:
        bfs_and_check(n, m, graph)
        return

    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    wall_dfs(cnt+1, n, m, graph)
                    graph[i][j] = 0

n, m = map(int, gets().split())
graph = [list(map(int, gets().split())) for _ in range(n)]

ans = 0
wall_dfs(0, n, m, graph)
print(ans)
