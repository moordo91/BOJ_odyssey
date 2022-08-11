import heapq
INF = float('inf')

def dijkstra(graph, start):
    heap = []
    cost_arr = [INF] * 100_001
    cost_arr[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        sec, now = heapq.heappop(heap)

        if sec > cost_arr[now]:
            continue

        for nxt_sec, nxt in graph[now]:
            cost = nxt_sec + sec

            if cost < cost_arr[nxt]:
                cost_arr[nxt] = cost
                heapq.heappush(heap, (cost, nxt))
    
    return cost_arr


n, k = map(int, input().split())

graph = {
    0: [(1, 1)],
    100_000: [(1, 99999)]
}

for i in range(1, 50_000+1):
    graph[i] = [(1, i-1), (1, i+1), (0, 2*i)]
    
for i in range(50_001, 100_000):
    graph[i] = [(1, i-1), (1, i+1)]

cost_arr = dijkstra(graph, n)
print(cost_arr[k])
