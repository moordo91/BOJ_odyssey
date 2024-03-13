import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

nearest = [start] * (n+1)
distance = [int(1e9)] * (n+1)
distance[start] = 0
queue = deque([(start, 0)])

while queue:
    now, cost = queue.popleft()
    
    if distance[now] < cost:
        continue
    
    for nxt, nxt_cost in graph[now]:
        if cost + nxt_cost < distance[nxt]:
            distance[nxt] = cost + nxt_cost
            nearest[nxt] = now
            queue.append((nxt, cost + nxt_cost))
        
path = []
temp = end
while temp != start:
    path.append(temp)
    temp = nearest[temp]
    
path.append(start)
path.reverse()

print(distance[end])
print(len(path))
print(*path)
