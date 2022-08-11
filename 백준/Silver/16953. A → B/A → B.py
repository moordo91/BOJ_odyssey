from collections import deque

class Node:
    
    def __init__(self, data, level):
        self.data = data
        self.level = level
        self.left = None
        self.right = None

start, target = map(int, input().split())
q = deque([Node(start, 1)])

while q:
    now = q.popleft()

    if now.data == target:
        print(now.level)
        exit(0)

    l = now.data * 2
    r = int(str(now.data)+"1")

    if l <= target:
        now.left = l
        q.append(Node(now.left, now.level+1))

    if r <= target:
        now.right = r
        q.append(Node(now.right, now.level+1))

print(-1)  