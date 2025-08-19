import sys
from collections import deque

input = sys.stdin.readline
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
ice = [(y, x) for y in range(M) for x in range(N) if grid[y][x] > 0]
year = 0

while ice:
    start = ice[0]
    q = deque([start])
    visited = set([start])
    melt = {}

    while q:
        y, x = q.popleft()
        sea = 0

        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < M and 0 <= nx < N:
                if grid[ny][nx] == 0:
                    sea += 1
                elif (ny, nx) not in visited and grid[ny][nx] > 0:
                    visited.add((ny, nx))
                    q.append((ny, nx))

        melt[(y, x)] = sea

    if len(visited) < len(ice):
        print(year)
        sys.exit(0)

    new_ice = []
    for y, x in ice:
        sea = melt.get((y, x), 0)
        h = grid[y][x] - sea
        if h > 0:
            grid[y][x] = h
            new_ice.append((y, x))
        else:
            grid[y][x] = 0
    ice = new_ice
    year += 1

print(0)
