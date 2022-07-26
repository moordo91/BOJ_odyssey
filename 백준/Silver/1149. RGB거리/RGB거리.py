import copy
import sys; gets = sys.stdin.readline

n = int(gets())
rgb = [0, 0, 0]
ans = [0, 0, 0]

for _ in range(n):
    rgb = copy.deepcopy(ans)
    r, g, b = map(int, gets().split())
    ans[0] = min(rgb[1], rgb[2]) + r
    ans[1] = min(rgb[0], rgb[2]) + g
    ans[2] = min(rgb[1], rgb[0]) + b

print(min(ans))
