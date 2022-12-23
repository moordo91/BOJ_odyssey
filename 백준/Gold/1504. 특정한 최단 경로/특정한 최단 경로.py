import sys, heapq
gets = sys.stdin.readline

def dijkstra(graph, start, destination):
    inf = float('inf')
    distances = [inf for _ in range(len(graph))]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (start, distances[start]))
    
    while queue:
        (current_destination, current_distance) = heapq.heappop(queue)
        
        if distances[current_destination] < current_distance:
            continue
        
        for (new_destination, new_distance) in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, (new_destination, distance))
        
    return distances[destination]

n, e = map(int, gets().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, gets().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int ,gets().split())

cost1 = dijkstra(graph, 1, v1) + dijkstra(graph, v1, v2) + dijkstra(graph, v2, n)
cost2 = dijkstra(graph, 1, v2) + dijkstra(graph, v2, v1) + dijkstra(graph, v1, n)
ans = min(cost1, cost2)

if type(ans) == int:
    print(ans)
else:
    print(-1)