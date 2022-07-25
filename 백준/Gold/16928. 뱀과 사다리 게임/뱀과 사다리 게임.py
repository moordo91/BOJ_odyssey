import sys; gets = sys.stdin.readline
from collections import deque

def input_route(graph, n):
    for _ in range(n):
        f, t = map(int, gets().split())
        graph[f] = set([t])
        for i in range(1, 100):
            if (i, f) in graph[i]:
                graph[i].remove((i, f))
                graph[i].add((i, t))

def bfs(graph, start):
    visited = [0] + [0 for _ in range(1, 100+1)]
    q = deque(graph[start])

    while q:
        (start, nxt) = q.popleft()
        if visited[nxt] == 0:
            q += graph[nxt]
            visited[nxt] = visited[start] + 1
    
    return visited


board = {i: set([(i, i+1), (i, i+2), (i, i+3), (i, i+4), (i, i+5), (i, i+6)])
        for i in range(1, 95)}

for i in range(95, 100+1):
    board[i] = set([(i, 100)])

N, M = map(int, gets().split())

input_route(board, N)
input_route(board, M)

visited = bfs(board, 1)

print(visited[100])