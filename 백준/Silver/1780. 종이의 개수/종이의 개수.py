import sys; ipt = sys.stdin.readline

ans = [0, 0, 0]

def check(p, y, x, n):

    for i in range(y, y+n):
        for j in range(x, x+n):
            if p[i][j] != p[y][x]:
                return False

    return True

def sol(p, y, x, n):

    if not check(p, y, x, n):
        n = n // 3
        for i in range(3):
            for j in range(3):
                sol(p, y + i*n, x + j*n, n)

    else:
        if p[y][x] < 0:
            ans[0] += 1
        elif p[y][x] > 0:
            ans[2] += 1
        else:
            ans[1] += 1


n = int(ipt())
p = [list(map(int, ipt().split())) for _ in range(n)]

sol(p, 0, 0, n)

for i in ans:
    print(i)