import sys
# from collections import deque
input = sys.stdin.readline

n = int(input())
sangeun = set(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

for i in card:
    if i in sangeun:
        print(1, end=' ')
    else:
        print(0, end=' ')


