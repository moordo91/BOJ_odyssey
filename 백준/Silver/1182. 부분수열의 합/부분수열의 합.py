import sys
from collections import deque
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

num = 2 ** n
count = 0
for i in range(1, num):
    w = list(map(int, [j for j in bin(i)[2:]]))
    w = [0] * (n - len(w)) + w
    k = 0
    for a, b in zip(arr, w):
        k += a * b
    if k == s:
        count += 1

print(count)