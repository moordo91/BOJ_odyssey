from math import comb

def trans(x, y, m):
    if x == 0:
        y.append(x%m)
        return
    trans(x//m, y, m)
    y.append(x%m)

u = []
d = []

n, k, m = map(int, input().split())
trans(n, u, m)
trans(k, d, m)

d = [0] * (len(u) - len(d)) + d
ans = 1

for i in range(len(u)):
    if u[i] < d[i]:
        print(0)
        exit(0)
    else:
        ans *= comb(u[i], d[i])

print(ans%m)