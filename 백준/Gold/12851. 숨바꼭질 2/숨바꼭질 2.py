import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, t, n):
    visited = [200000] * 100001
    queue = deque([(x, t)])
    finish = False
    while queue:
        x, t = queue.popleft()
        if x < 0 or x > 100000 or visited[x] < t:
            continue
        visited[x] = t
        if x == y:
            n += 1
            ans = t
            finish = True
        if not finish:
            if x < y:
                if x - 1 >= 0:
                    queue.append((x-1, t+1))
                queue.append((x+1, t+1))
                queue.append((2*x, t+1))
            else:
                queue.append((x-1, t+1))
    return ans, n

x, y = map(int, input().split())
t, n = bfs(x, y, 0, 0)
print(t)
print(n)

