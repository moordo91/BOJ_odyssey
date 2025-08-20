import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def is_connected(group, graph):
    q = deque([group[0]])
    visited = set([group[0]])

    while q:
        curr = q.popleft()
        for nxt in graph[curr]:
            if nxt in group and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    return len(visited) == len(group)


min_diff = float("inf")
N = int(input())
populations = list(map(int, input().split()))
total_population = sum(populations)
graph = [[] for _ in range(N)]
for i in range(N):
    links = list(map(int, input().split()))
    if len(links) == 1:
        continue
    for link in links[1:]:
        graph[i].append(link - 1)


for i in range(1, (N//2)+1):
    for group_A in combinations(range(N), i):
        group_B = tuple(node for node in range(N) if node not in group_A)
        
        if is_connected(group_A, graph) and is_connected(group_B, graph):
            population_A = sum(populations[node] for node in group_A)
            population_B = sum(populations[node] for node in group_B)
            min_diff = min(abs(population_A - population_B), min_diff)\

if min_diff == float('inf'):
    print(-1)
else:
    print(min_diff)
            