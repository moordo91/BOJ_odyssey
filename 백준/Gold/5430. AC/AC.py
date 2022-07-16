from collections import deque
import sys; gets = sys.stdin.readline

t = int(input())

for _ in range(t):
    cmd = gets().rstrip()
    n = int(input())
    arr = gets().rstrip()[1:-1].split(',')
    q = deque(arr)

    r, f, b, = 0, 0, len(q)-1
    flag = 0
    if n == 0:
        q = []
        f = 0
        b = 0

    for i in cmd:
        if i == 'R':
            r += 1
        elif i == 'D':
            if len(q) < 1:
                flag = 1
                print("error")
                break
            else:
                if r % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if flag == 0:
        if r % 2 == 0:
            print('[' + ','.join(q) + ']')
        else:
            q.reverse()
            print('[' + ','.join(q) + ']')