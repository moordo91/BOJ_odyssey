import sys; gets = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(gets())
graph = [[] for _ in range(n+1)]

def dfs(graph, distance, start, weight):
    for v_w in graph[start]:
        v, w = v_w
        if distance[v] == -1:
            distance[v] = weight + w
            dfs(graph, distance, v, distance[v])


for _ in range(n - 1):
    u, v, w = map(int, gets().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [-1] * (n+1)
dist[1] = 0
dfs(graph, dist, 1, 0)

farthest = dist.index(max(dist))
dist = [-1] * (n+1)
dist[farthest] = 0
dfs(graph, dist, farthest, 0)

print(max(dist))