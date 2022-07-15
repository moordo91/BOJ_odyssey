n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

ans = [0, 0, 0]

def sol(y, x, n):
    
    for i in range(y, y+n):
        for j in range(x, x+n):
            if p[i][j] != p[y][x]:
                for k in range(3):
                    for l in range(3):
                        sol(y + k*n//3, x + l*n//3, n//3)
                return
    if p[y][x] < 0:
        ans[0] += 1
    elif p[y][x] > 0:
        ans[2] += 1
    else:
        ans[1] += 1

sol(0, 0, n)

for i in ans: print(i)