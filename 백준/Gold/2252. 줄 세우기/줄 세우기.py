import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
    
answer = []
while q:
    x = q.popleft()
    answer.append(x)
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*answer)
  