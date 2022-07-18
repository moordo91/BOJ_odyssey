import sys; gets = sys.stdin.readline
from collections import deque

dic = {}

n, m = map(int, input().split())
for _ in range(n):
    web, pw = map(str, gets().rstrip().split())
    dic[web] = pw

for _ in range(m):
    print(dic[gets().rstrip()])