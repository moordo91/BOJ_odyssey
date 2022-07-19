t = int(input())
ans = []

def sol(x1, y1, x2, y2, planet):
    cnt = 0

    for circle in planet:
        cx, cy, r = circle
        
        d_start = (x1-cx)**2 + (y1-cy)**2
        d_end = (x2-cx)**2 + (y2-cy)**2
        
        if r**2 > max(d_start, d_end):
            continue
        elif r**2 < min(d_start, d_end):
            continue
        else:
            cnt += 1

    return cnt

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planet = [tuple(map(int, input().split())) for _ in range(n)]

    ans.append(sol(x1, y1, x2, y2, planet))

for i in ans:
    print(i)