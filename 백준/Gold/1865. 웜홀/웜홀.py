import sys; gets = sys.stdin.readline
INF = 1e9

def bellman_ford(n, e, graph, dist, start):
    dist[start] = 0

    for i in range(n):
        for j in range(e):
            now, nxt, wei = graph[j]

            if dist[nxt] > dist[now] + wei:
                dist[nxt] = dist[now] + wei
                if i == n-1:
                    return True
    return False

def sol(n, m, w):
    graph = []
    dist = [INF] * (n+1)

    for _ in range(m):
        s, e, t = map(int, gets().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, gets().split())
        graph.append((s, e, -t))
        
    if bellman_ford(n, 2*m+w, graph, dist, 1):
        print("YES")
    else:
        print("NO")

t = int(gets())

for _ in range(t):
    n, m, w = map(int, gets().split())
    sol(n, m, w)
    
