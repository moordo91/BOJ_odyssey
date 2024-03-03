import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])
for i in range(n):
    cmd = input().strip()
    if ' ' in cmd:
        cmd, num = cmd.split()
        num = int(num)
    if cmd == 'push':
        queue.append(num)
    elif cmd == 'pop':
        if queue:
            num = queue.popleft()
            print(num)
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        print(0) if queue else print(1)
    elif cmd == 'front':
        print(queue[0]) if queue else print(-1)
    elif cmd == 'back':
        print(queue[-1]) if queue else print(-1)