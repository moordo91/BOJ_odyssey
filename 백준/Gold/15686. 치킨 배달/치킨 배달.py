import sys; gets = sys.stdin.readline
from itertools import combinations
INF = 1e9

n, m = map(int, gets().split())
graph = [list(map(int, gets().split())) for _ in range(n)]

house = []
chick = []
ans = INF

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            house.append((y, x))
        elif graph[y][x] == 2:
            chick.append((y, x))

for c in combinations(chick, m):
    tmp = 0
    for h in house:
        chick_dist = INF
        for i in range(m):
            chick_dist = min(chick_dist, 
                             abs(h[0]-c[i][0]) + abs(h[1]-c[i][1]))
        tmp += chick_dist
    ans = min(ans, tmp)

print(ans)