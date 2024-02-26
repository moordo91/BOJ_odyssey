import sys
# from collections import deque
input = sys.stdin.readline

n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
max_weight = 0
for i in range(n):
    max_weight = max(max_weight, rope[i]*(i+1))

print(max_weight)
