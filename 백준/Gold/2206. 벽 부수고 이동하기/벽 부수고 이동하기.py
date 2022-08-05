from collections import deque
import sys; gets = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, n, m, visited):

    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, switch = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < m and 0 <= ny < n):
                continue

            if switch == 0 and graph[ny][nx] == 1:
                visited[ny][nx][1] = visited[y][x][0] + 1
                q.append((nx, ny, 1))

            elif graph[ny][nx] == 0 and visited[ny][nx][switch] == 0:
                visited[ny][nx][switch] = visited[y][x][switch] + 1
                q.append((nx, ny, switch))


n, m = map(int, gets().split())
graph = []
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, gets().rstrip())))

bfs(graph, n, m, visited)

if visited[-1][-1] == [0, 0]:
    print(-1)
elif visited[-1][-1][0] > 0 and visited[-1][-1][1] > 0:
    print(min(visited[-1][-1]))
else:
    print(max(visited[-1][-1]))