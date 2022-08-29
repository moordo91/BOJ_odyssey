import heapq
import sys; gets = sys.stdin.readline
INF = float('inf')

def dijkstra(n, start, graph):
    heap = []
    costArr = [INF] * (n+1)
    costArr[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)

        if cost > costArr[now]:
            continue

        for w, nxt in graph[now]:
            newCost = w + cost

            if newCost < costArr[nxt]:
                costArr[nxt] = newCost
                heapq.heappush(heap, (newCost, nxt))
    
    return costArr

n = int(gets())
m = int(gets())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, gets().split())
    graph[u].append((w, v))

start, end = map(int, gets().split())

costArr = dijkstra(n, start, graph)
print(costArr[end])