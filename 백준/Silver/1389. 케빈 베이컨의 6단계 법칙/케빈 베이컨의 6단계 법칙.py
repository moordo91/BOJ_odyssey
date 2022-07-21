import sys; gets = sys.stdin.readline

n, m = map(int, gets().split())
graph = [[float('inf') for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, gets().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

k_b = [sum(row) for row in graph]
print(k_b.index(min(k_b))+1)