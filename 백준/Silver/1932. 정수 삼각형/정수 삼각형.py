import sys; gets = sys.stdin.readline

n = int(gets())
t = [list(map(int, gets().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            t[i][j] = t[i][j] + t[i-1][0]
        elif j == i:
            t[i][j] = t[i][j] + t[i-1][j-1]
        else:
            t[i][j] = t[i][j] + max(t[i-1][j-1], t[i-1][j])

print(max(t[n-1]))