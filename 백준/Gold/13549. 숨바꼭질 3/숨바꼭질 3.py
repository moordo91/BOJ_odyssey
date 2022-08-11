from collections import deque

n, k = map(int, input().split())
q = deque([n])

MAX = 100_001
time = [-1] * MAX
time[n] = 0

while q:
    i = q.popleft()
    if i == k:
        print(time[i])
        break
    if i-1 >= 0 and time[i-1] == -1:
        q.append(i-1)
        time[i-1] = time[i] + 1
    if i*2 < MAX and time[i*2] == -1:
        q.appendleft(i*2)
        time[i*2] = time[i]
    if i+1 < MAX and time[i+1] == -1:
        q.append(i+1)
        time[i+1] = time[i] + 1
    