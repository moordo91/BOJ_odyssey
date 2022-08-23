import sys; gets = sys.stdin.readline
INF = float('inf')

n, m = map(int, gets().split())
graph = []
dist = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, gets().split())
    graph.append((u, v, w))

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            now, nxt, wei = graph[j]

            if dist[now] != INF and dist[nxt] > dist[now] + wei:
                dist[nxt] = dist[now] + wei
                if i == n-1:
                    return True

    return False

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])