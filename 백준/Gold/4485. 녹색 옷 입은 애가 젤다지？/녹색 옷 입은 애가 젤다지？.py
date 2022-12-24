from pprint import pprint
from heapq import heappush, heappop
import sys; gets = sys.stdin.readline

def map_generator(n: int, cave: list[list]) -> list[list]:
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    graph = [[[] for _ in range(n)] for _ in range(n)]    
    
    for y in range(n):
        for x in range(n):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if not (0<=ny<n and 0<=nx<n):
                    continue
                
                graph[y][x].append((cave[ny][nx], (ny, nx)))

    return graph

def dijkstra(n: int, graph: list[list], cave: list[list]) -> int:
    heap = []
    cost_arr = [[float('inf') for _ in range(n)] for _ in range(n)] 
    cost_arr[0][0] = cave[0][0]
    heappush(heap, (cost_arr[0][0], (0, 0)))
    
    while heap:
        cost, now = heappop(heap)
        
        if cost > cost_arr[now[0]][now[1]]:
            continue
        
        for w, nxt in graph[now[0]][now[1]]:
            new_cost = w + cost
            
            if new_cost < cost_arr[nxt[0]][nxt[1]]:
                cost_arr[nxt[0]][nxt[1]] = new_cost
                heappush(heap, (new_cost, nxt))
    
    return cost_arr[-1][-1]


t = 0
while 1:
    n = int(gets())
    if n == 0:
        break
    
    t += 1
    cave = []
    for _ in range(n):
        row = list(map(int, gets().split()))
        cave.append(row)
    
    graph = map_generator(n, cave)
    ans = dijkstra(n, graph, cave)
    print(f"Problem {t}: {ans}")
    
    