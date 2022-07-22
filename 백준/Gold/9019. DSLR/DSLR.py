from collections import deque
import sys; gets = sys.stdin.readline

def bfs(a, b, v):
    q = deque([(a, "")])
    v[a] = True

    while q:
        a, ans = q.popleft()
        if a == b:
            return ans
        
        n = a*2%10000
        if not v[n]:
            v[n] = True
            q.append((n, ans+"D"))
        
        n = (a-1)%10000
        if not v[n]:
            v[n] = True
            q.append((n, ans+"S"))

        n = (a//1000+a*10)%10000
        if not v[n]:
            v[n] = True
            q.append((n, ans+"L"))

        n = (a%10*1000+a//10)%10000
        if not v[n]:
            v[n] = True
            q.append((n, ans+"R"))

t = int(gets())
for _ in range(t):
    v = [False for _ in range(10000)]
    a, b = map(int, gets().split())
    print(bfs(a, b, v))