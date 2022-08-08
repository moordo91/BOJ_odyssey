import heapq
import sys; gets = sys.stdin.readline
INF = float('inf')

def dijkstra(n, start, graph):
    heap = []
    cost_arr = [INF] * n
    cost_arr[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        d, now = heapq.heappop(heap)

        for w, nxt in graph[now]:
            cost = w + d

            if cost < cost_arr[nxt]:
                cost_arr[nxt] = cost
                heapq.heappush(heap, (cost, nxt))
    
    return cost_arr

n, e = map(int, gets().split())
k = int(gets()) - 1

graph = [[] for _ in range(n)]

for _ in range(e):
    u, v, w = map(int, gets().split())
    u, v = u-1, v-1
    graph[u].append((w, v))

cost_arr = dijkstra(n, k, graph)

for i in cost_arr:
    if i == INF:
        print('INF')
    else:
        print(i)