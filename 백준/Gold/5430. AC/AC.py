from collections import deque
import sys; gets = sys.stdin.readline

t = int(gets())

for _ in range(t):
    cmd = deque(list(map(str, gets().strip())))
    end_switch = False
    rev_switch = 0
    n = int(gets())
    arr = gets().strip()
    if n > 0:
        arr = arr[1:-1].split(',')
        arr = deque(arr)
        while cmd:
            if cmd.popleft() == 'D':
                try:
                    if rev_switch % 2 == 0:
                        arr.popleft()
                    else:
                        arr.pop()
                except IndexError:
                    end_switch = True
                    print("error")
                    break
            else:
                rev_switch += 1
    
    else:
        if 'D' in cmd:
            print("error")
            continue
        else:
            end_switch = True
            print("[]")
    
    if end_switch:
        continue
    
    arr = list(arr)
    if rev_switch % 2 == 1:
        arr.reverse()
    if len(arr) > 0:
        print('[', end='')
        for i in range(len(arr)-1):
            print(arr[i], end=',')
        print(arr[-1], end=']\n')
    else:
        print("[]")