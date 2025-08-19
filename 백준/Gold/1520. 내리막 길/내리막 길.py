import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(graph, dp, y, x):
    if y == m - 1 and x == n - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    h = graph[y][x]
    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] < h:
            dp[y][x] += dfs(graph, dp, ny, nx)
    return dp[y][x]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

answer = dfs(graph, dp, 0, 0)
print(answer)