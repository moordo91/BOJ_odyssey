import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [1, 1]
for i in range(n):
    arr.append((arr[-1] + arr[-2]) % 15746)
    
print(arr[n])