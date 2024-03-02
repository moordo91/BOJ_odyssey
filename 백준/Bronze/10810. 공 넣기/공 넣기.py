import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * n
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a-1:b] = [c] * (b-a+1)

for i in range(n):
    print(arr[i], end=' ')