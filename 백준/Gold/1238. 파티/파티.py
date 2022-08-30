import heapq
import sys; gets = sys.stdin.readline

def dijkstra(n, graph, start, goal):
    heap = []
    costArr = [float('inf')] * (n+1)
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

    return costArr[goal]

n, m, x = map(int, gets().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, gets().split())
    graph[u].append((w, v))

ans = 0
for i in range(1, n+1):
    tmp = dijkstra(n, graph, i, x) + dijkstra(n, graph, x, i)
    if tmp > ans:
        ans = tmp

print(ans)