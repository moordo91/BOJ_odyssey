from collections import deque
import sys; gets = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(graph, dist, start):
    for v_w in graph[start]:
        v, w = v_w
        if dist[v] == -1:
            dist[v] = dist[start] + w
            dfs(graph, dist, v)

n = int(gets())
graph = [[] for _ in range(n+1)]

for i in range(n):
    edge = deque(list(map(int, gets().split()))[:-1])
    start = edge.popleft()
    for _ in range(len(edge)//2):
        v = edge.popleft()
        w = edge.popleft()
        graph[start].append((v, w))

dist1 = [-1] * (n+1)
dist2 = [-1] * (n+1)
dist1[1] = 0

dfs(graph, dist1, 1)
max_dist1 = max(dist1)
max_dist1_index = dist1.index(max_dist1)
dist2[max_dist1_index] = 0

dfs(graph, dist2, max_dist1_index)
print(max(dist2))
