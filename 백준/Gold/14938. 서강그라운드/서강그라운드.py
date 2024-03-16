import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
items = [0] + items

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

max_items = [0 for _ in range(n+1)]
for i in range(1, n+1):
    visitable = [i for i, v in enumerate(graph[i]) if v <= m]
    for j in visitable:
        max_items[i] += items[j]
        
print(max(max_items))