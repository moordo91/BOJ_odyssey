import sys
input = sys.stdin.readline

input_lines = []
rows, cols = map(int, input().split())
for i in range(rows):
    line = input()
    input_lines.append(line)
graph = [list(input_lines[i]) for i in range(rows)]
visited = [False] * 26
level = 1
max_level = 1

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x, level):
    if visited[ord(graph[y][x])-65]:
        return
    global max_level
    max_level = max(max_level, level)
    visited[ord(graph[y][x])-65] = True
    # print(stk)
    for i in range(4):
        nx, ny = y + dy[i], x + dx[i]
        if 0 <= nx < rows and 0 <= ny < cols:
            dfs(nx, ny, level + 1)
    visited[ord(graph[y][x])-65] = False
    # print(stk)


dfs(0, 0, max_level)
print(max_level)