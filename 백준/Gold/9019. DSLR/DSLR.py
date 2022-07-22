from collections import deque
import sys; gets = sys.stdin.readline

def bfs(node, end, visited):
    q = deque([(node, "")])
    visited[node] = True

    while q:
        node, ans = q.popleft()
        if node == end:
            return ans


        num = (2*node) % 10000
        if not visited[num]:
            visited[num] = True
            q.append((num, ans+"D"))
        
        num = (node-1) % 10000
        if not visited[num]:
            visited[num] = True
            q.append((num, ans+"S"))

        num = (node*10 + (node//1000)) % 10000        
        if not visited[num]:
            visited[num] = True
            q.append((num, ans+"L"))
            
        num = ((node%10)*1000 + (node//10)) % 10000
        if not visited[num]:
            visited[num] = True
            q.append((num, ans+"R"))

t = int(gets())

for _ in range(t):
    visited = [False for _ in range(10000)]
    start, end = map(int, gets().split())
    print(bfs(start, end, visited))