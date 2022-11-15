import sys, math
ipt = sys.stdin.readline

def cal_d(x, y):
    d = y - x
    k = math.floor(d**0.5)
    if d >= k*(k+1) + 1:
        print(2*k+1)
    elif d >= k*k + 1:
        print(2*k)
    else:
        print(2*k-1)

n = int(ipt())

for i in range(n):
    a, b = map(int, ipt().split())
    cal_d(a, b)