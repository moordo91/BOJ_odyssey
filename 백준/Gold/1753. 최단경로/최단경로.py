import heapq
import sys; gets = sys.stdin.readline
INF = float('inf')


def dijkstra(n, start, graph):
    heap = []
    result = [INF] * n
    result[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        d, now = heapq.heappop(heap)

        if result[now] < d:
            continue

        for v, w in graph[now]:
            cost = w + d

            if cost < result[v]:
                result[v] = cost
                heapq.heappush(heap, (cost, v))

    return result


n, e = map(int, gets().split())

k = int(gets()) - 1

graph = [[] for _ in range(n)]
for _ in range(e):
    u, v, w = map(int, gets().split())
    u, v= u-1, v-1
    graph[u].append((v, w))


result = dijkstra(n, k, graph)

for i in result:
    if i == INF:
        print('INF')
    else:
        print(i)
