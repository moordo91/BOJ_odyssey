import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = set(arr[1:])
party = []
for i in range(m):
    party.append(list(map(int, input().split()))[1:])

for i in range(n):
    for j in range(m):
        if set(party[j]) & arr:
            arr = arr.union(party[j])

print(sum(1 for i in party if arr.isdisjoint(i)))
